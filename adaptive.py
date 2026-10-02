"""
adaptive.py — the brain of ECET Mentor.
Weak-topic detection + mastery tracking + daily plan generation.
No external deps: runs on attempt history in SQLite.
"""
import json
from collections import defaultdict
from datetime import date
from db import get_conn

# How many practice questions per topic per day
DAILY_PER_TOPIC = 3


def topic_stats(student_id: int) -> dict:
    """{topic: {subject, attempts, correct, mastery(0-1), streak}} using ALL history,
    with recent weight (last 10 attempts per topic) mattering more."""
    conn = get_conn()
    rows = conn.execute("""
        SELECT q.topic, q.subject, a.correct, a.created_at
        FROM attempts a JOIN questions q ON q.id = a.question_id
        WHERE a.student_id = ?
        ORDER BY a.created_at DESC
    """, (student_id,)).fetchall()
    conn.close()

    stats = defaultdict(lambda: {"attempts": 0, "correct": 0, "recent": []})
    for r in rows:
        s = stats[r["topic"]]
        s["attempts"] += 1
        s["correct"] += r["correct"]
        s["subject"] = r["subject"]
        if len(s["recent"]) < 10:
            s["recent"].append(r["correct"])
    out = {}
    for topic, s in stats.items():
        acc = s["correct"] / s["attempts"] if s["attempts"] else 0
        recent_acc = (sum(s["recent"]) / len(s["recent"])) if s["recent"] else acc
        mastery = round(0.5 * acc + 0.5 * recent_acc, 3)  # recent performance dominates
        out[topic] = {
            "subject": s["subject"], "attempts": s["attempts"],
            "correct": s["correct"], "accuracy": round(acc, 3),
            "mastery": mastery,
        }
    return out


def weak_topics(student_id: int, top_n: int = 5) -> list:
    """Lowest-mastery topics with at least 3 attempts (else anything attempted)."""
    stats = topic_stats(student_id)
    eligible = [(t, s) for t, s in stats.items() if s["attempts"] >= 3]
    pool = eligible if eligible else list(stats.items())
    ranked = sorted(pool, key=lambda kv: (kv[1]["mastery"], -kv[1]["attempts"]))
    return [t for t, _ in ranked[:top_n]]


def next_difficulty(student_id: int, topic: str) -> int:
    """Adaptive difficulty: mastery < 0.4 → easy(1), < 0.7 → medium(2), else hard(3)."""
    m = topic_stats(student_id).get(topic, {}).get("mastery", 0)
    return 1 if m < 0.4 else (2 if m < 0.7 else 3)


def pick_questions(student_id: int, topic: str, n: int = DAILY_PER_TOPIC) -> list:
    conn = get_conn()
    diff = next_difficulty(student_id, topic)
    rows = conn.execute("""
        SELECT id FROM questions
        WHERE topic = ? AND difficulty BETWEEN ? AND ?
          AND id NOT IN (
              SELECT question_id FROM attempts
              WHERE student_id = ? AND correct = 1
          )
        ORDER BY RANDOM() LIMIT ?
    """, (topic, diff, min(3, diff + 1), student_id, n)).fetchall()
    if len(rows) < n:  # relax: allow already-correct ones
        rows += conn.execute("""
            SELECT id FROM questions WHERE topic = ?
              AND id NOT IN (SELECT ?)
            ORDER BY RANDOM() LIMIT ?
        """, (topic, rows and rows[0]["id"] or 0, n - len(rows))).fetchall()
    conn.close()
    return [r["id"] for r in rows]


def pick_bank_questions(track: str | None = None, only_pyq: bool = False,
                        min_years: int = 1, n: int = 1, exclude: set | None = None) -> list:
    """Random questions from the whole bank, optionally filtered by track / PYQ.

    only_pyq + min_years=2 -> the 'Last 10 Years Repeated Questions' pool.
    """
    conn = get_conn()
    where, args = [], []
    if track and track != "all":
        where.append("track = ?")
        args.append(track)
    if only_pyq:
        where.append("is_pyq = 1 AND pyq_count >= ?")
        args.append(min_years)
    sql = "SELECT id FROM questions"
    if where:
        sql += " WHERE " + " AND ".join(where)
    sql += " ORDER BY RANDOM() LIMIT ?"
    args.append(max(n * 3, n))
    rows = [r["id"] for r in conn.execute(sql, args).fetchall()]
    conn.close()
    if exclude:
        rows = [q for q in rows if q not in exclude]
    return rows[:n]


def generate_daily_plan(student_id: int, day: str | None = None) -> list:
    """One plan per day: 3 weak topics × 3 questions. Idempotent per (student, day)."""
    day = day or date.today().isoformat()
    conn = get_conn()
    existing = conn.execute(
        "SELECT topic, subject, question_ids FROM daily_plans WHERE student_id=? AND day=?",
        (student_id, day)).fetchall()
    if existing:
        conn.close()
        return [{"topic": r["topic"], "subject": r["subject"],
                 "question_ids": json.loads(r["question_ids"])} for r in existing]

    weak = weak_topics(student_id, top_n=3)
    plan = []
    for t in weak:
        subj = topic_stats(student_id).get(t, {}).get("subject", "")
        qids = pick_questions(student_id, t)
        if qids:
            cur = conn.execute(
                "INSERT INTO daily_plans (student_id, day, topic, subject, question_ids) VALUES (?,?,?,?,?)",
                (student_id, day, t, subj, json.dumps(qids)))
            plan.append({"topic": t, "subject": subj, "question_ids": qids})
    conn.commit()
    conn.close()
    return plan


def xp_and_streak(student_id: int) -> dict:
    """Gamification: XP = 10 per correct attempt; streak = consecutive active days."""
    conn = get_conn()
    xp_row = conn.execute(
        "SELECT COUNT(*) c FROM attempts WHERE student_id=? AND correct=1",
        (student_id,)).fetchone()
    days = [r["d"] for r in conn.execute(
        "SELECT DISTINCT substr(created_at,1,10) d FROM attempts WHERE student_id=? ORDER BY d DESC",
        (student_id,))]

    streak = 0
    from datetime import date as _d, timedelta as _td
    day = _d.today()
    day_set = set(days)
    while day.isoformat() in day_set:
        streak += 1
        day -= _td(days=1)

    mocks = conn.execute(
        "SELECT score FROM mocks WHERE student_id=? AND score IS NOT NULL ORDER BY started_at",
        (student_id,)).fetchall()
    conn.close()
    return {
        "xp": xp_row["c"] * 10,
        "streak": streak,
        "mocks": [m["score"] for m in mocks],
        "improvement": (mocks[-1]["score"] - mocks[0]["score"]) if len(mocks) >= 2 else 0,
    }

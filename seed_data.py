"""
seed_data.py — ECET Mentor: loads the English-only question bank + simulated cohort.

Real ECET pattern: Mathematics 50 · Physics 25 · Chemistry 25 · Engineering (branch) 100.
Question bank lives in bank_math / bank_physics / bank_chemistry / bank_engg (see question_bank.py):
    Mathematics 112 · Physics 110 · Chemistry 100 · Engineering (CSE) 110  ->  432 total
Run:  miniconda3/python.exe seed_data.py
"""
import json
import random
from datetime import datetime, timedelta

from db import get_conn, init_db, DB_PATH
import question_bank

random.seed(42)

BRANCH_ENGG = {
    "CSE": ["C Programming", "Data Structures", "Operating Systems", "DBMS", "Computer Networks"],
}

NAMES = ["Aarav", "Bhavana", "Charan", "Divya", "Eswar", "Fatima", "Ganesh", "Harika", "Imran", "Jyothi",
         "Kiran", "Lakshmi", "Mahesh", "Nandini", "Omkar", "Pavani", "Qadir", "Ramya", "Sai Teja", "Thanmai",
         "Uma", "Vijay", "Waseem", "Xavier", "Yashoda", "Zainab", "Anil", "Bhargav", "Chandana", "Deepak",
         "Eshita", "Farhan", "Gouri", "Harshith", "Indira", "Jagan", "Keerthana", "Lohith", "Meghana", "Nikhil"]


def seed():
    if DB_PATH.exists():
        DB_PATH.unlink()
    init_db()
    conn = get_conn()
    cur = conn.cursor()

    # ---------- questions (options shuffled, correct letter tracked) ----------
    for r in question_bank.ALL:
        opts = r["options"][:]
        correct_text = opts[r["correct_idx"]]
        random.shuffle(opts)
        new_cor = "abcd"[opts.index(correct_text)]
        years = r["pyq_years"]
        year_list = [int(y) for y in years.split(",")] if years else []
        a, b, c, d = opts
        cur.execute("""INSERT INTO questions
            (subject,topic,track,q_en,q_te,opt_a,opt_b,opt_c,opt_d,correct,difficulty,
             is_pyq,pyq_year,pyq_years,pyq_count,explanation_en,explanation_te)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (r["subject"], r["topic"], r["track"], r["q_en"], None, a, b, c, d, new_cor,
             r["difficulty"], 1 if years else 0, max(year_list) if year_list else None,
             years, len(year_list), r["explanation"], None))

    cur.execute("SELECT id, track, topic FROM questions")
    by_topic = {}
    for qid, track, topic in cur.fetchall():
        by_topic.setdefault((track, topic), []).append(qid)

    topics = question_bank.topics_by_track()
    # subject lookup per (track, topic)
    subj_of = {(r["track"], r["topic"]): r["subject"] for r in question_bank.ALL}
    practice_topics = [t for t in topics["math"] + topics["engg"] + topics["physics"] + topics["chemistry"]]

    # ---------- students ----------
    branches = ["CSE", "ECE", "EEE"]
    for i, nm in enumerate(NAMES):
        cur.execute("INSERT INTO students (name, roll_no, branch, lang) VALUES (?,?,?,?)",
                    (nm, f"DIP23-{i+1:03d}", branches[i % 3], "en"))
    sids = [r[0] for r in cur.execute("SELECT id FROM students").fetchall()]

    today = datetime(2026, 10, 2)

    # ---------- 21 days of adaptive practice ----------
    for sid in sids:
        weak = random.sample(practice_topics, 4)
        skill = {t: random.uniform(0.30, 0.55) for t in weak}
        for day in range(20, -1, -1):
            d = today - timedelta(days=day)
            stamp = d.strftime("%Y-%m-%d %H:%M:%S")
            topics_today = weak if day % 3 == 0 else random.sample(weak, 2)
            for t in topics_today:
                tr = next(tr for tr in ("math", "engg", "physics", "chemistry") if t in topics[tr])
                pool = by_topic.get((tr, t), [])
                if not pool:
                    continue
                for qid in random.sample(pool, min(2, len(pool))):
                    p_correct = min(0.93, skill[t] + (21 - day) * 0.014)
                    ok = random.random() < p_correct
                    cur.execute("""INSERT INTO attempts
                        (student_id,question_id,chosen,correct,seconds,mode,created_at)
                        VALUES (?,?,?,?,?,?,?)""",
                        (sid, qid, "a" if ok else random.choice(["b", "c", "d"]),
                         1 if ok else 0, random.randint(18, 70), "practice", stamp))
                cur.execute("""INSERT OR IGNORE INTO daily_plans
                    (student_id,day,topic,subject,question_ids,completed)
                    VALUES (?,?,?,?,?,1)""",
                    (sid, d.strftime("%Y-%m-%d"), t, subj_of.get((tr, t), tr), json.dumps(pool[:2])))
        # two mock tests with improvement
        m1 = round(random.uniform(45, 62), 1)
        m2 = round(min(93, m1 + random.uniform(11, 24)), 1)
        for score, days_ago in ((m1, 14), (m2, 2)):
            stamp = (today - timedelta(days=days_ago)).strftime("%Y-%m-%d %H:%M:%S")
            cur.execute("""INSERT INTO mocks (student_id,started_at,submitted_at,score,total_q)
                           VALUES (?,?,?,?,20)""", (sid, stamp, stamp, score))

    conn.commit()
    stats = {t: cur.execute("SELECT COUNT(*) FROM questions WHERE track=?", (t,)).fetchone()[0]
             for t in ("math", "physics", "chemistry", "engg")}
    pyq = cur.execute("SELECT COUNT(*) FROM questions WHERE is_pyq=1").fetchone()[0]
    n_a = cur.execute("SELECT COUNT(*) FROM attempts").fetchone()[0]
    conn.close()
    print(f"Seeded: {sum(stats.values())} questions {stats} | {pyq} PYQ | 40 students | {n_a} attempts | 80 mocks")


if __name__ == "__main__":
    seed()

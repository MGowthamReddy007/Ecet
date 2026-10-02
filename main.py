"""
main.py — ECET Mentor FastAPI backend.
Run:  miniconda3/python.exe -m uvicorn main:app --port 8000
"""
import json
import random
from contextlib import asynccontextmanager
from datetime import date, timedelta
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

from db import init_db, get_conn
import adaptive
import tutor

BASE = Path(__file__).parent


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    # Self-contained boot: if the DB has no questions (e.g. a fresh cloud deploy),
    # seed the question bank + demo cohort so the app works with zero setup.
    try:
        conn = get_conn()
        empty = conn.execute("SELECT COUNT(*) FROM questions").fetchone()[0] == 0
        conn.close()
    except Exception:
        empty = True
    if empty:
        import seed_data
        seed_data.seed()
    yield

app = FastAPI(title="ECET Mentor API", version="1.0", lifespan=lifespan)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


# ---------- auth-free demo session ----------
class LoginReq(BaseModel):
    name: str
    roll_no: str
    branch: str = "CSE"
    lang: str = "both"


class AnswerReq(BaseModel):
    student_id: int
    question_id: int
    chosen: str
    seconds: int = 0
    mode: str = "practice"
    lang: str = "both"


class MockStartReq(BaseModel):
    name: str | None = None
    roll_no: str
    branch: str = "CSE"
    lang: str = "en"
    mode: str = "quick"  # quick (20 Q) | full (real 200-Q ECET pattern)


class MockSubmitReq(BaseModel):
    mock_id: int
    answers: dict  # {question_id: "a"}


def _ensure_student(roll_no: str, name: str | None = None, branch: str | None = None, lang: str = "both"):
    conn = get_conn()
    row = conn.execute("SELECT * FROM students WHERE roll_no=?", (roll_no,)).fetchone()
    if not row:
        conn.execute("INSERT INTO students (name, roll_no, branch, lang) VALUES (?,?,?,?)",
                     (name or f"Student {roll_no}", roll_no, branch or "CSE", lang))
        conn.commit()
        row = conn.execute("SELECT * FROM students WHERE roll_no=?", (roll_no,)).fetchone()
    elif name:
        conn.execute("UPDATE students SET name=?, lang=COALESCE(?,lang) WHERE id=?",
                     (name, lang, row["id"]))
        conn.commit()
    d = dict(row)
    conn.close()
    return d


def _q_dict(r, lang: str = "both") -> dict:
    d = dict(r)
    show_te = lang in ("te", "both")
    if not show_te:
        d["question"] = d["q_en"]
    else:
        d["question"] = d["q_en"] if not d["q_te"] else (d["q_en"] if lang == "both" else d["q_te"])
    return d


# ---------------- auth ----------------
@app.post("/api/login")
def login(req: LoginReq):
    s = _ensure_student(req.roll_no, req.name, req.branch, req.lang)
    return {"student": s}


# ---------------- practice ----------------
@app.get("/api/practice/{student_id}")
def practice(student_id: int, lang: str = "en", mode: str = "adaptive",
             track: str = "all", subject: str = "all"):
    """Next practice question.

    mode=adaptive -> weak-topic plan + adaptive difficulty (default)
    mode=model    -> random from the full model bank (optional track/subject filter)
    mode=pyq      -> 'Last 10 Years Repeated Questions' (appeared in 2+ years)
    """
    conn = get_conn()

    if mode in ("model", "pyq"):
        where, args = [], []
        if track and track != "all":
            where.append("track = ?"); args.append(track)
        if subject and subject != "all":
            where.append("subject = ?"); args.append(subject)
        if mode == "pyq":
            where.append("is_pyq = 1 AND pyq_count >= 2")
        sql = "SELECT * FROM questions"
        if where:
            sql += " WHERE " + " AND ".join(where)
        sql += " ORDER BY RANDOM() LIMIT 1"
        row = conn.execute(sql, args).fetchone()
        if not row:
            conn.close()
            raise HTTPException(404, "no questions match this filter")
        n_pool = conn.execute(
            "SELECT COUNT(*) FROM questions" + ((" WHERE " + " AND ".join(where)) if where else ""),
            args).fetchone()[0]
        conn.close()
        q = _q_dict(row, lang)
        return {"question": q, "difficulty": row["difficulty"], "pool_size": n_pool, "mode": mode}

    # adaptive (default)
    plan = conn.execute(
        "SELECT question_ids FROM daily_plans WHERE student_id=? AND day=? AND completed=0",
        (student_id, date.today().isoformat())).fetchall()
    pool = []
    done = {r["question_id"] for r in conn.execute(
        "SELECT question_id FROM attempts WHERE student_id=? AND mode='practice' AND date(created_at)=?",
        (student_id, date.today().isoformat())).fetchall()}
    for p in plan:
        ids = json.loads(p["question_ids"])
        pool += [q for q in ids if q not in done]
    if not pool:
        weak = adaptive.weak_topics(student_id, top_n=3)
        for t in weak:
            pool += adaptive.pick_questions(student_id, t, n=2)
    if not pool:
        pool = [r["id"] for r in conn.execute(
            "SELECT id FROM questions ORDER BY RANDOM() LIMIT 5").fetchall()]
    qid = random.choice(pool)
    row = conn.execute("SELECT * FROM questions WHERE id=?", (qid,)).fetchone()
    conn.close()
    if not row:
        raise HTTPException(404, "no questions")
    q = _q_dict(row, lang)
    return {"question": q, "difficulty": row["difficulty"], "pool_size": len(pool), "mode": "adaptive"}


@app.post("/api/answer")
def answer(req: AnswerReq):
    conn = get_conn()
    row = conn.execute("SELECT * FROM questions WHERE id=?", (req.question_id,)).fetchone()
    if not row:
        raise HTTPException(404, "question not found")
    ok = 1 if req.chosen == row["correct"] else 0
    conn.execute("""INSERT INTO attempts (student_id,question_id,chosen,correct,seconds,mode)
                    VALUES (?,?,?,?,?,?)""",
                 (req.student_id, req.question_id, req.chosen, ok, req.seconds, req.mode))
    conn.commit()
    conn.close()
    q = dict(row)
    exp = tutor.explain(q, req.lang)
    stats = adaptive.xp_and_streak(req.student_id)
    return {
        "correct": bool(ok),
        "correct_option": row["correct"],
        "explanation": exp["text"],
        "explanation_source": exp["source"],
        "xp": stats["xp"], "streak": stats["streak"],
    }


@app.get("/api/plan/{student_id}")
def plan(student_id: int):
    p = adaptive.generate_daily_plan(student_id)
    stats = adaptive.xp_and_streak(student_id)
    return {"plan": p, "xp": stats["xp"], "streak": stats["streak"]}


# ---------------- mock test ----------------
@app.post("/api/mock/start")
def mock_start(req: MockStartReq):
    """Mock drawn from the practice bank.

    quick -> 20 Q  (Math 5, Physics 3, Chemistry 2, Engineering 10)
    full  -> 200 Q real ECET pattern (Math 50, Physics 25, Chemistry 25, Engineering 100)
    """
    s = _ensure_student(req.roll_no, req.name, req.branch, req.lang)
    quick = req.mode != "full"
    pattern = (("math", 5), ("physics", 3), ("chemistry", 2), ("engg", 10)) if quick \
        else (("math", 50), ("physics", 25), ("chemistry", 25), ("engg", 100))
    conn = get_conn()
    picks = []
    for track, n in pattern:
        rows = conn.execute(
            "SELECT * FROM questions WHERE track=? ORDER BY RANDOM() LIMIT ?",
            (track, n)).fetchall()
        picks += rows
    random.shuffle(picks)
    cur = conn.execute("INSERT INTO mocks (student_id, total_q) VALUES (?,?)",
                       (s["id"], len(picks)))
    mock_id = cur.lastrowid
    conn.commit()
    conn.close()
    return {"mock_id": mock_id, "student": s,
            "questions": [dict(r) for r in picks]}


@app.post("/api/mock/submit")
def mock_submit(req: MockSubmitReq):
    conn = get_conn()
    mock = conn.execute("SELECT * FROM mocks WHERE id=?", (req.mock_id,)).fetchone()
    if not mock:
        raise HTTPException(404, "mock not found")
    student_id = mock["student_id"]
    total = mock["total_q"]
    correct = sum(1 for qid, ch in req.answers.items()
                  if conn.execute("SELECT correct FROM questions WHERE id=?", (int(qid),)).fetchone()["correct"] == ch)
    score = round(100 * correct / total, 1)
    conn.execute("UPDATE mocks SET submitted_at=datetime('now'), score=? WHERE id=?",
                 (score, req.mock_id))
    for qid, ch in req.answers.items():
        row_c = conn.execute("SELECT correct FROM questions WHERE id=?", (int(qid),)).fetchone()
        conn.execute("""INSERT INTO attempts (student_id,question_id,chosen,correct,seconds,mode,mock_id)
                        VALUES (?,?,?,?,?,?,?)""",
                     (student_id, int(qid), ch, 1 if row_c and row_c["correct"] == ch else 0,
                      0, "mock", req.mock_id))
    conn.commit()
    conn.close()
    return {"score": score, "correct": correct, "total": total}


# ---------------- analytics ----------------
@app.get("/api/practice-progress/{student_id}")
def practice_progress(student_id: int):
    """How much of the practice bank this student has covered, per track + PYQ progress."""
    conn = get_conn()
    tracks = []
    acc_tries = acc_ok = 0
    for track, label in (("math", "Mathematics"), ("physics", "Physics"),
                         ("chemistry", "Chemistry"), ("engg", "Engineering")):
        total = conn.execute("SELECT COUNT(*) FROM questions WHERE track=?", (track,)).fetchone()[0]
        row = conn.execute("""
            SELECT COUNT(DISTINCT a.question_id) attempted, COUNT(*) tries, SUM(a.correct) ok
            FROM attempts a JOIN questions q ON q.id=a.question_id
            WHERE a.student_id=? AND q.track=?
        """, (student_id, track)).fetchone()
        attempted, tries, ok = row["attempted"] or 0, row["tries"] or 0, row["ok"] or 0
        pyq_total = conn.execute(
            "SELECT COUNT(*) FROM questions WHERE track=? AND is_pyq=1 AND pyq_count>=2",
            (track,)).fetchone()[0]
        pyq_done = conn.execute("""
            SELECT COUNT(DISTINCT a.question_id) FROM attempts a JOIN questions q ON q.id=a.question_id
            WHERE a.student_id=? AND q.track=? AND q.is_pyq=1 AND q.pyq_count>=2
        """, (student_id, track)).fetchone()[0] or 0
        acc_tries += tries
        acc_ok += ok
        tracks.append({
            "track": track, "label": label, "total": total, "attempted": attempted,
            "coverage": round(100 * attempted / total, 1) if total else 0,
            "accuracy": round(100 * ok / tries, 1) if tries else 0,
            "pyq_total": pyq_total, "pyq_done": pyq_done,
        })
    bank_total = conn.execute("SELECT COUNT(*) FROM questions").fetchone()[0]
    bank_done = conn.execute(
        "SELECT COUNT(DISTINCT question_id) FROM attempts WHERE student_id=?", (student_id,)).fetchone()[0]
    conn.close()
    return {
        "tracks": tracks,
        "bank_total": bank_total, "bank_attempted": bank_done,
        "bank_coverage": round(100 * bank_done / bank_total, 1) if bank_total else 0,
        "overall_accuracy": round(100 * acc_ok / acc_tries, 1) if acc_tries else 0,
    }


@app.get("/api/progress/{student_id}")
def progress(student_id: int):
    conn = get_conn()
    s = conn.execute("SELECT * FROM students WHERE id=?", (student_id,)).fetchone()
    if not s:
        raise HTTPException(404, "student not found")

    daily = conn.execute("""
        SELECT date(created_at) d, COUNT(*) total, SUM(correct) ok
        FROM attempts WHERE student_id=? GROUP BY d ORDER BY d
    """, (student_id,)).fetchall()
    subjects = conn.execute("""
        SELECT q.subject, COUNT(*) total, SUM(a.correct) ok
        FROM attempts a JOIN questions q ON q.id=a.question_id
        WHERE a.student_id=? GROUP BY q.subject
    """, (student_id,)).fetchall()
    topics = conn.execute("""
        SELECT q.topic, q.subject, COUNT(*) total, SUM(a.correct) ok
        FROM attempts a JOIN questions q ON q.id=a.question_id
        WHERE a.student_id=? GROUP BY q.topic ORDER BY total DESC
    """, (student_id,)).fetchall()
    mocks = conn.execute(
        "SELECT score, started_at FROM mocks WHERE student_id=? AND score IS NOT NULL ORDER BY started_at",
        (student_id,)).fetchall()
    conn.close()

    stats = adaptive.xp_and_streak(student_id)
    weak = adaptive.weak_topics(student_id, top_n=5)

    # ---- rank among the whole cohort (by XP) + leaderboard for the Progress page ----
    conn2 = get_conn()
    ranked = conn2.execute("""
        SELECT s.id, s.name, s.roll_no, s.branch, COUNT(a.correct)*10 xp
        FROM students s LEFT JOIN attempts a ON a.student_id=s.id
        GROUP BY s.id ORDER BY xp DESC
    """).fetchall()
    order = [dict(r) for r in ranked]
    my_rank = next((i + 1 for i, r in enumerate(order) if r["id"] == student_id), None)
    my_row = next((r for r in order if r["id"] == student_id), None)
    conn2.close()

    return {
        "student": dict(s),
        "xp": stats["xp"], "streak": stats["streak"],
        "rank": my_rank, "cohort_size": len(order),
        "my_xp": my_row["xp"] if my_row else 0,
        "leaderboard": order[:10],
        "daily": [dict(r) for r in daily],
        "subjects": [{"subject": r["subject"],
                      "accuracy": round(100 * (r["ok"] or 0) / r["total"], 1)} for r in subjects],
        "topics": [{"topic": r["topic"], "subject": r["subject"],
                    "mastery": round(100 * (r["ok"] or 0) / r["total"], 1),
                    "attempts": r["total"]} for r in topics],
        "mock_scores": [m["score"] for m in mocks],
        "weak_topics": weak,
        "improvement": stats["improvement"],
    }


@app.get("/api/cohort")
def cohort():
    """Impact stats for judges: how many students improved, average gain, leaderboard."""
    conn = get_conn()
    rows = conn.execute("""
        SELECT s.name, s.roll_no, s.branch,
               MIN(m.score) first_score,
               MAX(m.score) last_score,
               COUNT(m.score) n_mocks
        FROM students s JOIN mocks m ON m.student_id=s.id
        GROUP BY s.id HAVING n_mocks >= 2
    """).fetchall()
    improved = [dict(r) for r in rows if r["last_score"] > r["first_score"]]
    gains = [r["last_score"] - r["first_score"] for r in improved]
    leaderboard = conn.execute("""
        SELECT s.name, s.roll_no, s.branch, SUM(a.correct)*10 xp
        FROM students s JOIN attempts a ON a.student_id=s.id
        GROUP BY s.id ORDER BY xp DESC LIMIT 10
    """).fetchall()
    n_students = conn.execute("SELECT COUNT(*) FROM students").fetchone()[0]
    active = conn.execute("SELECT COUNT(DISTINCT student_id) FROM attempts").fetchone()[0]
    conn.close()
    return {
        "students_total": n_students,
        "students_active": active,
        "students_improved": len(improved),
        "improvement_rate": round(100 * len(improved) / max(1, n_students), 1),
        "avg_gain": round(sum(gains) / len(gains), 1) if gains else 0,
        "best_gain": max(gains) if gains else 0,
        "leaderboard": [dict(r) for r in leaderboard],
    }


@app.get("/api/bank/meta")
def bank_meta():
    """Subjects/topics and PYQ counts per track — powers the practice filters."""
    conn = get_conn()
    rows = conn.execute("""
        SELECT track, subject, COUNT(*) n,
               SUM(CASE WHEN is_pyq=1 AND pyq_count>=2 THEN 1 ELSE 0 END) repeated,
               SUM(is_pyq) pyq
        FROM questions GROUP BY track, subject ORDER BY track, subject
    """).fetchall()
    counts = {r["track"]: r["n"] for r in conn.execute(
        "SELECT track, COUNT(*) n FROM questions GROUP BY track").fetchall()}
    pyq_counts = {r["track"]: r["n"] for r in conn.execute(
        "SELECT track, COUNT(*) n FROM questions WHERE is_pyq=1 AND pyq_count>=2 GROUP BY track").fetchall()}
    conn.close()
    tracks = {}
    for r in rows:
        tracks.setdefault(r["track"], {"subjects": []})["subjects"].append(
            {"subject": r["subject"], "count": r["n"], "repeated": r["repeated"] or 0, "pyq": r["pyq"] or 0})
    for tr, v in tracks.items():
        v["count"] = counts.get(tr, 0)
        v["repeated"] = pyq_counts.get(tr, 0)
    return {"tracks": tracks, "total": sum(counts.values()),
            "total_repeated": sum(pyq_counts.values())}


# ---------------- static frontend ----------------
@app.get("/")
def index():
    return FileResponse(BASE / "static" / "index.html")


@app.get("/health")
def health():
    return {"status": "ok", "app": "ECET Mentor", "db": str((BASE / "ecet_mentor.db").exists())}

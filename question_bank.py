"""
question_bank.py — combines the per-subject banks into one uniform structure.

Uniform record (dict):
    {subject, topic, track, q_en, options:[4], correct_idx, difficulty, pyq_years, explanation}

Counts: Mathematics 112, Physics 110, Chemistry 100, Engineering (CSE) 110 -> 432 total.
"""
from collections import OrderedDict

import bank_math
import bank_physics
import bank_chemistry
import bank_engg


def _rows():
    out = []
    # math / physics / chemistry: (topic, q, opts, correct, diff, pyq, exp)
    for mod in (bank_math, bank_physics, bank_chemistry):
        for (topic, q, opts, correct, diff, pyq, exp) in mod.BANK:
            out.append({
                "subject": mod.SUBJECT, "topic": topic, "track": mod.TRACK,
                "q_en": q, "options": opts, "correct_idx": correct,
                "difficulty": diff, "pyq_years": pyq, "explanation": exp,
            })
    # engineering: (subject, topic, q, opts, correct, diff, pyq, exp)
    for (subject, topic, q, opts, correct, diff, pyq, exp) in bank_engg.BANK:
        out.append({
            "subject": subject, "topic": topic, "track": bank_engg.TRACK,
            "q_en": q, "options": opts, "correct_idx": correct,
            "difficulty": diff, "pyq_years": pyq, "explanation": exp,
        })
    return out


ALL = _rows()


def topics_by_track() -> dict:
    """{track: [topics in first-seen order]} derived from the actual bank."""
    d = OrderedDict()
    for r in ALL:
        d.setdefault(r["track"], [])
        if r["topic"] not in d[r["track"]]:
            d[r["track"]].append(r["topic"])
    return d


def summary() -> dict:
    s = {}
    for r in ALL:
        s.setdefault(r["track"], {"total": 0, "pyq": 0, "topics": set()})
        s[r["track"]]["total"] += 1
        s[r["track"]]["topics"].add(r["topic"])
        if r["pyq_years"]:
            s[r["track"]]["pyq"] += 1
    return {k: {"total": v["total"], "pyq": v["pyq"], "topics": len(v["topics"])}
            for k, v in s.items()}


if __name__ == "__main__":
    total = 0
    for k, v in summary().items():
        print(f"{k:10s} total={v['total']:4d}  pyq={v['pyq']:4d}  topics={v['topics']}")
        total += v["total"]
    print("TOTAL", total)

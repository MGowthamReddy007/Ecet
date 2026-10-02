"""
db.py — SQLite helpers for ECET Mentor.
"""
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "ecet_mentor.db"


def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    """Create tables from schema.sql if the database is fresh."""
    fresh = not DB_PATH.exists()
    conn = get_conn()
    if fresh:
        schema = (Path(__file__).parent / "schema.sql").read_text(encoding="utf-8")
        conn.executescript(schema)
        conn.commit()
    conn.close()
    return fresh


if __name__ == "__main__":
    print("Fresh DB created:", init_db())

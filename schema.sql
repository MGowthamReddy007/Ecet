-- ECET Mentor database schema
CREATE TABLE IF NOT EXISTS students (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    name          TEXT NOT NULL,
    roll_no       TEXT UNIQUE NOT NULL,
    branch        TEXT NOT NULL,          -- CSE / ECE / EEE / MECH / CIVIL
    lang          TEXT DEFAULT 'en',      -- 'en' | 'te' | 'both'
    created_at    TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS questions (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    subject       TEXT NOT NULL,          -- Mathematics / Physics / Chemistry / C Programming ...
    topic         TEXT NOT NULL,          -- Weak-topic granularity
    track         TEXT NOT NULL,          -- math(50) / physics(25) / chemistry(25) / engg(100)
    q_en          TEXT NOT NULL,          -- question in English
    q_te          TEXT,                   -- question in Telugu
    opt_a         TEXT, opt_b TEXT, opt_c TEXT, opt_d TEXT,
    correct       TEXT NOT NULL,          -- 'a'|'b'|'c'|'d'
    explanation_en TEXT,
    explanation_te TEXT,
    difficulty    INTEGER DEFAULT 1,      -- 1 easy, 2 medium, 3 hard
    is_pyq        INTEGER DEFAULT 0,      -- from previous-year paper
    pyq_year      INTEGER,                -- most recent year it appeared
    pyq_years     TEXT,                   -- comma list, e.g. '2019,2021,2023'
    pyq_count     INTEGER DEFAULT 0       -- how many years it repeated (frequency)
);
CREATE INDEX IF NOT EXISTS idx_questions_track ON questions(track);
CREATE INDEX IF NOT EXISTS idx_questions_pyq ON questions(is_pyq);

CREATE TABLE IF NOT EXISTS attempts (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id    INTEGER NOT NULL REFERENCES students(id),
    question_id   INTEGER NOT NULL REFERENCES questions(id),
    chosen        TEXT,                   -- NULL = skipped
    correct       INTEGER NOT NULL,       -- 1/0
    seconds       INTEGER DEFAULT 0,
    mode          TEXT DEFAULT 'practice',-- practice | mock
    mock_id       INTEGER,
    created_at    TEXT DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_attempts_student ON attempts(student_id, created_at);

CREATE TABLE IF NOT EXISTS daily_plans (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id    INTEGER NOT NULL REFERENCES students(id),
    day           TEXT NOT NULL,          -- 'YYYY-MM-DD'
    topic         TEXT NOT NULL,
    subject       TEXT NOT NULL,
    question_ids  TEXT NOT NULL,          -- JSON list
    completed     INTEGER DEFAULT 0,
    UNIQUE(student_id, day, topic)
);

CREATE TABLE IF NOT EXISTS mocks (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id    INTEGER NOT NULL REFERENCES students(id),
    started_at    TEXT DEFAULT (datetime('now')),
    submitted_at  TEXT,
    score         REAL,                   -- 0..100
    total_q       INTEGER NOT NULL
);

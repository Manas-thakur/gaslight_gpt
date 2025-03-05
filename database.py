from app import connect_db
with connect_db() as conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            name TEXT NOT NULL,
            phone TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            prompt_count INTEGER DEFAULT 0
        )
    """)
import sqlite3

conn = sqlite3.connect("emails.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email_type TEXT,
    content TEXT
)
""")

conn.commit()


def save_email(email_type, content):
    cursor.execute(
        "INSERT INTO history (email_type, content) VALUES (?, ?)",
        (email_type, content)
    )
    conn.commit()


def get_history():
    cursor.execute("SELECT * FROM history ORDER BY id DESC")
    return cursor.fetchall()
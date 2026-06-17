import sqlite3

conn = sqlite3.connect("emails.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS emails (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    email_type TEXT,
    content TEXT
)
""")

conn.commit()


def save_email(user, email_type, content):
    cursor.execute(
        "INSERT INTO emails (user, email_type, content) VALUES (?, ?, ?)",
        (user, email_type, content)
    )
    conn.commit()


def get_user_emails(user):
    cursor.execute("SELECT * FROM emails WHERE user=? ORDER BY id DESC", (user,))
    return cursor.fetchall()
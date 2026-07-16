import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

email = "anoshaoad5@gmail.com"  # the email you signed up with

cursor.execute("UPDATE users SET is_admin = 1 WHERE email = ?", (email,))

conn.commit()
conn.close()
print("Admin access granted!")
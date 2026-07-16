import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM books")
print("Total books:", cursor.fetchone()[0])

cursor.execute("SELECT title FROM books")
print("Book titles:", [row[0] for row in cursor.fetchall()])

cursor.execute("SELECT COUNT(*) FROM articles")
print("Total articles:", cursor.fetchone()[0])

conn.close()
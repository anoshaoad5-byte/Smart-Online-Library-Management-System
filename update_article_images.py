import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

image_updates = [
    ("/static/images/publiclib.jpg", "The Value of Public Libraries in Modern Education"),
     ("/static/images/studyrotiune.jpg", "How to Build a Consistent Study Routine"),
]

for image_url, title in image_updates:
    cursor.execute(
        "UPDATE articles SET image = ? WHERE title = ?",
        (image_url, title)
    )

conn.commit()
conn.close()
print("Article images updated successfully!")
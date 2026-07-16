import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

articles = [
    ("Why Reading Habits Matter More Than Ever", "Library Insights",
     "In a world full of distractions, setting aside just 20 minutes a day for reading can improve focus, vocabulary, and empathy. Studies consistently show that regular readers develop stronger critical thinking skills and a deeper understanding of different perspectives, making reading one of the simplest yet most powerful daily habits anyone can build.",
     "PASTE_IMAGE_URL_HERE",
     "July 2026"),

    ("The Rise of Digital Libraries", "Library Insights",
     "Digital libraries are transforming how people access knowledge, breaking down barriers of geography and cost. With just an internet connection, students and researchers can now reach thousands of books, journals, and research papers instantly. This shift is especially valuable in regions where physical libraries are limited, opening doors to education that were previously closed.",
     "PASTE_IMAGE_URL_HERE",
     "July 2026"),

    ("How to Build a Consistent Study Routine", "Study Tips",
     "Consistency beats intensity when it comes to studying. Rather than cramming for hours once a week, breaking study sessions into shorter, regular blocks helps information move into long-term memory more effectively. Pairing a fixed study time with a distraction-free space can make even 30 minutes a day surprisingly productive.",
     "PASTE_IMAGE_URL_HERE",
     "July 2026"),

    ("The Value of Public Libraries in Modern Education", "Education Today",
     "Public libraries remain one of the most underrated resources in a student's education. Beyond just books, they offer quiet study spaces, access to research databases, and often free workshops or tutoring. Supporting and using local libraries helps sustain these community resources for future generations of learners.",
     "PASTE_IMAGE_URL_HERE",
     "July 2026")
]

cursor.executemany(
    "INSERT INTO articles(title,source,content,image,published_date) VALUES(?,?,?,?,?)",
    articles
)

conn.commit()
conn.close()
print("4 articles added successfully!")
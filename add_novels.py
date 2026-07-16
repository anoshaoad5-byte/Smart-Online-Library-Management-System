import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

novels = [
    ("The Alchemist", "Paulo Coelho", "750RS",
     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSzS6br2VcsslRW1Ld1iDJ6bB2DyvWz7tU-AFlAAiU0Iw&s=10",
     "A shepherd boy's journey to fulfill his personal legend, exploring themes of destiny, dreams, and self-discovery.",
     "fiction"),

    ("To Kill a Mockingbird", "Harper Lee", "850RS",
     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTMPK41hpJQdaRDdxIF8RaJGF6IOFJLA8RbdH4JYLnTqA&s=10",
     "A powerful story of racial injustice and moral growth seen through the eyes of a young girl in the American South.",
     "fiction"),

    ("The Kite Runner", "Khaled Hosseini", "800RS",
     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0Q5iOFeuGg0SvJBGxVKSyxOEe7fBEjkTMUcc_PeWsXg&s=10",
     "A tale of friendship, guilt, and redemption set against the backdrop of Afghanistan's turbulent history.",
     "fiction"),

    ("A Man Called Ove", "Fredrik Backman", "700RS",
     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQ9_r_jkBwdvpmT2H1q5SANyVRXntZDcr3jXl5_l2Ieg&s=10",
     "A grumpy yet lovable widower's life is transformed by new neighbors in this heartwarming story about grief and connection.",
     "fiction"),

    ("The Old Man and the Sea", "Ernest Hemingway", "650RS",
     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYUhrpwXvUPZSMNK_r06myYrp04hsd6qCsKX0YYi_gAw&s=10",
     "An aging fisherman's epic battle with a giant marlin, a meditation on perseverance and human dignity.",
     "fiction")
]

cursor.executemany(
    "INSERT INTO books(title,author,price,image,description,category) VALUES(?,?,?,?,?,?)",
    novels
)

conn.commit()
conn.close()
print("5 novels added successfully!")
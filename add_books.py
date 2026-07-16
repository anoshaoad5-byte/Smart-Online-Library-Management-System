import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

new_books = [
    ("Bang-e-Dara", "Allama Iqbal", "600RS",
     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTo9I9hYRQKbahS4YS_bTbtYxdAYLJNr_epLYkfAuT1xw&s=10",
     "Iqbal's first Urdu poetry collection, written over twenty years, blending Persian mysticism with the call for self-awareness and reform.",
     "fiction"),

    ("Romeo and Juliet", "William Shakespeare", "700RS",
     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS70dbr_7WSp1ApbfeHbAbvAG-H7eZZMHPgJ5e2ByRlbw&s=10",
     "Shakespeare's timeless tragedy of two young lovers whose deaths ultimately reconcile their feuding families.",
     "fiction"),

    ("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "900RS",
     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQE0Tjohx401B08YYfdIt9v_iBm38TDHKbD5e77C72n_A&s=10",
     "The first book in the Harry Potter series, following a young wizard's journey as he discovers his magical heritage.",
     "fiction")
]

cursor.executemany(
    "INSERT INTO books(title,author,price,image,description,category) VALUES(?,?,?,?,?,?)",
    new_books
)

conn.commit()
conn.close()
print("3 new books added successfully!")
import sqlite3
from flask import Flask, render_template, request, flash, redirect, url_for, session
    

app = Flask(__name__)
app.secret_key = "mysecretkey"

def init_db():
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
        """)
        # Add is_admin column if it doesn't already exist
        cursor.execute("PRAGMA table_info(users)")
        columns = [col[1] for col in cursor.fetchall()]
        if "is_admin" not in columns:
            cursor.execute("ALTER TABLE users ADD COLUMN is_admin INTEGER DEFAULT 0")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            price TEXT NOT NULL,
            image TEXT NOT NULL,
            description TEXT NOT NULL,
            category TEXT NOT NULL
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            source TEXT NOT NULL,
            content TEXT NOT NULL,
            image TEXT,
            published_date TEXT
        )
        """)

        cursor.execute("SELECT COUNT(*) FROM books")
        if cursor.fetchone()[0] == 0:
            sample_books = [
                ("Python Programming", "John Smith", "1000RS",
                 "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSAoxuo3r4anamx0W5YDqtccSvA8ALz331PMYsgTDjgqA&s=10",
                 "Learn Python from beginner to advanced with practical examples.",
                 "technology"),
                ("History of Pakistan", "Ian Talbot", "800RS",
                 "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQti9ixQBdmLO3KWBJPjZGVl9i1eUP8WbPNVbdWAqxe4Q&s=10",
                 "A complete history of Pakistan from independence to the modern era.",
                 "history"),
                ("Artificial Intelligence", "Stuart Russell", "999RS",
                 "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRfBURr7DgHfgqj8CorMipM-K-JMJN_dWWUrpkx-k8-Fw&s=10",
                 "Introduction to Artificial Intelligence and Machine Learning.",
                 "science")
            ]
            cursor.executemany(
                "INSERT INTO books(title,author,price,image,description,category) VALUES(?,?,?,?,?,?)",
                sample_books
            )

        conn.commit()
        conn.close()

@app.route("/")
def home():
    username = session.get("user")

    conn = sqlite3.connect("library.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    books = cursor.execute("SELECT * FROM books").fetchall()
    articles = cursor.execute("SELECT * FROM articles").fetchall()
    conn.close()

    return render_template("index.html", username=username, books=books, articles=articles)

         
@app.route("/login", methods=["GET", "POST"])
def login():

        if request.method == "POST":
            email = request.form["email"]
            password = request.form["password"]

            conn = sqlite3.connect("library.db")
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            user = cursor.execute(
                "SELECT * FROM users WHERE email=? AND password=?",
                (email, password)
            ).fetchone()

            conn.close()

            if user:
                session["user"] = user["fullname"]
                flash(f"Welcome, {user['fullname']}!")
                return redirect(url_for("home"))
            else:
                flash("Invalid Email or Password!")
                return redirect(url_for("login"))

        return render_template("login.html")

@app.route("/logout")
def logout():
        session.pop("user", None)
        flash("You have been logged out successfully!")
        return redirect(url_for("home"))


@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        fullname = request.form["fullname"]
        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email=?",
            (email,)
        )

        user = cursor.fetchone()

        if user:
            flash("Email already registered!")
            conn.close()
            return redirect(url_for("signup"))

        cursor.execute(
            "INSERT INTO users(fullname,email,password) VALUES(?,?,?)",
            (fullname,email,password)
        )

        conn.commit()
        conn.close()

        flash("Registration Successful!")
        return redirect(url_for("signup"))

    return render_template("signup.html")

@app.route("/admin")
def admin_dashboard():
    if not session.get("user"):
        flash("Please login first!")
        return redirect(url_for("login"))

    conn = sqlite3.connect("library.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    user = cursor.execute(
        "SELECT * FROM users WHERE fullname = ?", (session["user"],)
    ).fetchone()

    if not user or user["is_admin"] != 1:
        flash("Access denied. Admins only!")
        conn.close()
        return redirect(url_for("home"))

    books = cursor.execute("SELECT * FROM books").fetchall()
    articles = cursor.execute("SELECT * FROM articles").fetchall()
    users = cursor.execute("SELECT * FROM users").fetchall()

    conn.close()

    return render_template("admin.html", books=books, articles=articles, users=users)



init_db()
if __name__ == "__main__":
     app.run(debug=True)


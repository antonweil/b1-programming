import sqlite3

conn = sqlite3.connect("/Users/antonweil/Documents/GitHub/b1-programming/other/database.db")

cursor = conn.cursor()

cursor.execute("""
	CREATE TABLE IF NOT EXISTS users (
		id INTEGER PRIMARY KEY,
		name TEXT NOT NULL,
		age INTEGER
	)
""")

new_user = ("Alice", 28)

cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", new_user)

cursor.execute("""SELECT * FROM users""")
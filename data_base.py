import sqlite3

conn = sqlite3.connect("dbm1.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE  IF NOT EXISTS student_feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    feedback_text TEXT,
    date TEXT
)
""") 

cursor.execute("""
CREATE TABLE IF NOT EXISTS supervisors(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fname TEXT,
    lname TEXT,
    username TEXT UNIQUE,
    email TEXT UNIQUE,
    password TEXT
)
""")

cursor.execute("""

CREATE TABLE IF NOT EXISTS resulte (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    resulte_text TEXT,
    date TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS counter (
    id INTEGER PRIMARY KEY,
    visits INTEGER
)
""")

cursor.execute("SELECT COUNT(*) FROM counter")
count = cursor.fetchone()[0]
if count == 0:
    cursor.execute("INSERT INTO counter (id, visits) VALUES (1, 0)")

cursor.execute("SELECT * FROM  student_feedback")
data = cursor.fetchall()
for i in data :
  print (i)

conn.commit()
conn.close()

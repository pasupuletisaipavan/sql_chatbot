import sqlite3

db_path = "data/databases/school.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Check Students table
cursor.execute("SELECT * FROM Students;")
print("Students:", cursor.fetchall())

# Check Marks table
cursor.execute("SELECT * FROM Marks;")
print("Marks:", cursor.fetchall())

conn.close()
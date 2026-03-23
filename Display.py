import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="college"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM student")

for row in cursor.fetchall():
    print(row)

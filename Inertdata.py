import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="college"
)

cursor = conn.cursor()

sql = "INSERT INTO student(name, age, course) VALUES (%s, %s, %s)"
values = ("Chinmayi", 22, "MCA")

cursor.execute(sql, values)
conn.commit()

print("Data inserted successfully")

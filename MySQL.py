import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = conn.cursor()

# Create Database
cursor.execute("CREATE DATABASE college")

print("Database created successfully")
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="college"
)

cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE student(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    age INT,
    course VARCHAR(50)
)
""")

print("Table created successfully")

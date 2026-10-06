import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root@123",
    database="quiz_exam_db"
)

print("MySQL connected successfully!")
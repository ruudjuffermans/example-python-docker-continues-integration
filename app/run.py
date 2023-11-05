import os
import mysql.connector
import env


connection = mysql.connector.connect(
    user=os.environ["DB_USER"], password=os.environ["DB_PASS"], host=os.environ["DB_HOST"], port=os.environ["DB_PORT"], database=os.environ["DB_NAME"])


for key, value in os.environ.items():
    print(f'{key}: {value}')
cursor = connection.cursor()
cursor.execute('Select * FROM Students')
students = cursor.fetchall()
connection.close()

print(students)

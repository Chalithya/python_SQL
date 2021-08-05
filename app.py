# import mysql.connector
import sys
import pyodbc 


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=FLOKI;'
                      'Database=testDB;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM testDB.dbo.Take')

for row in cursor:
    print(row)

# db = mysql.connector.connect(
#     host="localhost",
#     user="newuser",
#     passwd=""
# )


# mycursor = db.cursor()

# mycursor.execute("CREATE DATABASE pythonDB")
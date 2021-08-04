import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)


mycursor = db.cursor()

mycursor.execute("CREATE DATABASE pythonDB")
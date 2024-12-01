import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="testuser",
  password="multipass"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

mycursor.execute("CREATE TABLE index (name VARCHAR(255), email VARCHAR(255))")

mycursor.execute("SELECT emails FROM table GROUP BY emails HAVING COUNT(*) > 1")
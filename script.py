import mysql.connector
import os
import getpass
usr=str(getpass.getuser())
pswd=getpass.getpass()
mydb = mysql.connector.connect(
    host="localhost",
    username=usr,
    password=pswd
)

mycursor=mydb.cursor()

mycursor.execute("CREATE DATABASE calendarApp")
mydb = mysql.connector.connect(
    host="localhost",
    username=usr,
    password=pswd,
    database="calendarApp"
)
mycursor=mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS events (SlNo INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255), date DATE, description VARCHAR(255))")

import mysql.connector
import os
import getpass


pswd=getpass.getpass("Enter password :")

mydb = mysql.connector.connect(
  host="localhost",
  user=str(getpass.getuser()),
  password=pswd,
  database="calendarApp"
)

mycursor = mydb.cursor()

sql = "INSERT INTO events (name, date, description) VALUES (%s, %s, %s)"

na = str(input("Enter event name : "))
desc = str(input("Enter event description : "))
dt = str(input("Enter date [format -> {YYYY-MM-DD}]  :"))
dt = dt.strip()


val = (na,dt,desc)
mycursor.execute(sql, val)
mydb.commit()

print("Record Inserted.")

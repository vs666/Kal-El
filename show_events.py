import os
import getpass
from tabulate import tabulate
import mysql.connector
from datetime import datetime


now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d')


pswd=getpass.getpass("Enter password :")
try:
  mydb = mysql.connector.connect(
    host="localhost",
    user=str(getpass.getuser()),
    password=str(pswd),
    database="calendarApp"
  )

except:
  print("Something is not right....")
  exit()
mycursor = mydb.cursor()

sql = "SELECT * FROM events WHERE date ='"+str(formatted_date)+"'"
mycursor.execute(sql)

myresult = mycursor.fetchall()

'''

    for playing of sound sox is necessary
    sudo apt install sox

'''


duration = 1  # seconds
freq = 440  # Hz
os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))

print("TODAY'S EVENTS")
print(80*"-")
print(tabulate(myresult,headers=["Sl. No", "Task","Date", "Details"]))
print(80*"-")


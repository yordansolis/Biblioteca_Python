#Seleccione registro(s) donde la dirección sea "Park Lane 38": resultado:
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()
#selecciona el Ocean balvd 2
sql = "SELECT * FROM usuario  WHERE address = %s"
val = ("Ocean blvd 2", )
mycursor.execute(sql, val)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
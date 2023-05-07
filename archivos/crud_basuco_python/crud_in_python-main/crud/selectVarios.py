import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database ="mydatabase"
)

#ahora inicamos la db
mycurso = mydb.cursor()

#Nota: Usamos el fetchall() método, que obtiene todas las filas de la última declaración ejecutada.
mycurso.execute("SELECT nombre, address FROM usuario ORDER BY nombre")
myresult = mycurso.fetchall()

for x in myresult:
  print(x)
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database ="mydatabase"
)


#ahora inicamos la db
mycurso = mydb.cursor()



sql = "UPDATE usuario SET address = %s WHERE address = %s"
val = ("Asprilal@gmail.com", "SOLOSYORDA@gmail.com")


mycurso.execute(sql, val)

mydb.commit()

print(mycurso.rowcount, "record(s) affected")
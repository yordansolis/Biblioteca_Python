import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database ="mydatabase"
)


#ahora inicamos la db
mycurso = mydb.cursor()



sql = "DELETE FROM usuario WHERE address = %s"
val = ("Lowstreet 4", )
mycurso.execute(sql, val)

mydb.commit()

print(mycurso.rowcount, "record(s) deleted")
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database ="mydatabase"
)

#ahora inicamos la db
mycurso = mydb.cursor()

sql = "INSERT INTO usuario(nombre, address) VALUES (%s, %s)"
val = ("Juanme", "mena@gmail.com")

mycurso.execute(sql, val)
#esta cimmit es obligatoria
mydb.commit()

#esto nos devuelve 1
print(mycurso.rowcount)


#asi inservamos varios arreglos


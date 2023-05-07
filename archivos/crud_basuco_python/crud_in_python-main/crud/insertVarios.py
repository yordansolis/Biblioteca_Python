import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database ="mydatabase"
)


#ahora inicamos la db
mycurso = mydb.cursor()



#asi inservamos varios arreglos
sql = "INSERT INTO usuario(nombre, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2')
  ]

mycurso.executemany(sql, val)
mydb.commit()

#esto nos devuelve 1
print(mycurso.rowcount)



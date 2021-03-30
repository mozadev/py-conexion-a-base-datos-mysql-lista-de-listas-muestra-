import mysql as mysql
import pymysql

db = pymysql.connect(host='localhost', user='root', password='', database='user')



cursor = db.cursor()
sql = "INSERT INTO datos(Correo,Clave) VALUES('prueba@gmail.com','prueba22')"
cursor.execute(sql)
db.commit()
cursor.execute("SELECT * from datos")

# Fetch all the rows in a list of lists.
resultados = cursor.fetchall()
for row in resultados:
    id = row[0]
    correo = row[1]
    clave = row[2]
    print ("Id: ", id, " Correo: ", correo,"Clave: ",clave)

db.close()
# conexiones__bbdd
Paquete completo de conexiones a bases de datos como oracle, mysql, sqlserver y sqlite con python

Instalar para el modulo de mysql pymysql

	pip install PyMySQL

Instalar para el modulo de oracle

	pip install cx_Oracle

Instalar para el modulo de sqlite

	pip install sqlite3

Instalar para el modulo sqlserver

	pip install pyodbc

Hay un archivo llamado scriptTabla.sql que es un pequeño script en mysql para crear la tabla con los datos necesarios para que funcione el script mysql, pero hay que tener en cuenta que para hacer las comprobaciones y que todo funcione correctamente has de tener instalado cada servidor y creada la bbdd con su tabla y sus datos.

Los parametro que recibe el modulo mysql son:

	host: Nombre del servidor al que quieres conectar
	user: Usuario que uses
	password: Contraseña que tengas
	dataBase : Nombre de tu base de datos
	port: puerto de la base de datos, por defecto 3306
	charset: Codificación de la bbdd, por defecto UTF-8


Los parametro que recibe el modulo oracle son:

	host: Nombre del servidor al que quieres conectar
	user: Usuario que uses
	password: Contraseña que tengas
	port: puerto de la base de datos
	tsname: el tsname de oracle, normalmente es xe en oracle expres edition

Los parametros para sqlite son:

	dataBase : Nombre de tu base de datos

Los parametros para sqlServer son:

	driver:
	server: Nombre del servidor al que quieres conectar
	dataBase : Nombre de tu base de datos
	user: Usuario que uses
	password: Contraseña que tengas

Ejemplo de GRUD con mysql

	import mysql

	# De esta forma evitamos el sql Inyection.
	select = "SELECT NOMBRE_ARTICULO, PRECIO FROM PRODUCTOS WHERE id=%s"
	whereSelect = "1"
	#Insert
	insert = "INSERT INTO PRODUCTOS (NOMBRE_ARTICULO, PRECIO) VALUES (%s, %s)"
	valInsert = [("prueba python", 40)]

	#Update
	update = "UPDATE PRODUCTOS SET NOMBRE_ARTICULO=%s, PRECIO=%s WHERE id=%s"
	valUpdate = ("prueba python update", 50, 5)

	# Delete
	delete = "DELETE FROM PRODUCTOS WHERE id in (%s)"
	whereDelete = ('5')


	con = mysql.Mysql("localhost", "chenox", "123456", "GestionProductos")
	data = con.select(select, whereSelect)

	print ("Datos : {0}".format(data))

	con.insert(insert, valInsert)
	con.update(update,valUpdate)
	con.delete(delete, whereDelete)

	# desconecta del servidor
	con.close_connect()
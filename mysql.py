import pymysql

class Mysql():
	"""Esta clase conecta con la base de datos,
	ademas tambien podemos hacer insert, select, delete y update"""

	def __init__(self, host, user, password, database, port=3306, charset='utf8'):
		"""Constructor de la clase"""
		self.__host = host
		self.__user = user
		self.__password = password
		self.__database = database
		self.__port = port
		self.__charset = charset

		self.__connect()


	def __connect (self):
		"""Conecta a la base de datos"""
		try:
			self.db = pymysql.connect(host=self.__host,
								port = self.__port,
								user=self.__user,
								passwd=self.__password,
								db=self.__database,
								charset=self.__charset)
			self.__cursor()
		except Exception as e:
		    # Atrapar error
		    print("Ocurrió un error al conectar a Mysql: ", e)

	def __cursor (self):
		""" Creamos el cursor
		Funcion solo accesible desde el objeto BBDD"""
		try:
			self.cursor = self.db.cursor()
		except Exception as e:
		    # Atrapar error
		    print("Ocurrió un error al crear el cursor: ", e)

	def close_connect(self):
		self.db.close()
		print("Conexión cerrada")

	def insert (self, sql, val):
		"""Insertamos en la base de datos

		>>> t.insert("INSERT INTO PRODUCTOS (NOMBRE_ARTICULO, PRECIO, SECCION) VALUES (%s, %s, %s)", [("prueba python", 40, "python")])
		1 record inserted.
		"""
		try:
			self.cursor.executemany(sql, val)
			self.db.commit()
			print(self.cursor.rowcount, "record inserted.")
		except Exception as e:
		    # Atrapar error
		    print("Ocurrió un error al insertar: ", e)

	def update (self, sql, val):
		""" Actualizamos en la base de datos

		>>> t.update("UPDATE PRODUCTOS SET NOMBRE_ARTICULO=%s, PRECIO=%s WHERE SECCION=%s", ("prueba python update", 50, "python"))
		Actualizado correctamente.
		"""
		try:
			self.cursor.execute(sql, val)
			self.db.commit()
			print("Actualizado correctamente.")
		except Exception as e:
		    # Atrapar error
		    print("Ocurrió un error al actualizar: ", e)

	def delete (self, sql, noInyect):
		""" Borramos en la base de datos

		>>> t.delete ("DELETE FROM PRODUCTOS WHERE SECCION = %s", ("python"))
		Borrado correctamente.

		"""
		try:
			self.cursor.execute(sql, noInyect)
			self.db.commit()
			print("Borrado correctamente.")
		except Exception as e:
		    # Atrapar error
		    print("Ocurrió un error al borrar: ", e)

	def select (self, sql, noInyect=None):
		"""Recogemos datos de la base de datos

		>>> t.select("SELECT NOMBRE_ARTICULO, PRECIO FROM PRODUCTOS WHERE id=%s", "1")
		(('Pelota', 35),)

		"""
		try:
			if noInyect is None:
				self.cursor.execute(sql)
			else:
				self.cursor.execute(sql, noInyect)
			return self.cursor.fetchall()
		except Exception as e:
		    # Atrapar error
		    print("Ocurrió un error al recoger los datos: ", e)

if __name__ == "__main__":
	import doctest
	doctest.testmod(extraglobs={'t': Mysql("localhost", "chenox", "123456", "GestionProductos")})
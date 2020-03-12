import pyodbc

class Sqlserver():
	"""Esta clase conecta con la base de datos,
	ademas tambien podemos hacer insert, select, delete y update"""

	def __init__(self, driver, server, database, user, password):
		"""Constructor de la clase"""
		self.__driver = driver
		self.__server = server
		self.__database = database
		self.__user = user
		self.__password = password

		self.__connect()

	def __connect (self):
		"""Conecta a la base de datos"""
		try:
			self.db = pyodbc.connect('DRIVER={'+self.__driver+'};'
									'SERVER=' +self.__server+';'
	                              	'DATABASE='+self.__database+';'
	                              	'UID='+self.__user+';'
	                              	'PWD=' + self.__password+';')
			self.__cursor()
		except Exception as e:
		    # Atrapar error
		    print("Ocurrió un error al conectar a SQL Server: ", e)

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

		>>> t.insert("INSERT INTO PRODUCTOS (NOMBRE_ARTICULO, PRECIO, SECCION) VALUES (?, ?, ?)", ("prueba python", 40, "python"))
		1 record inserted.
		"""
		try:
			self.cursor.execute(sql, val)
			print(self.cursor.rowcount, "record inserted.")
		except Exception as e:
		    # Atrapar error
		    print("Ocurrió un error al insertar: ", e)

	def update (self, sql, val):
		""" Actualizamos en la base de datos

		>>> t.update("UPDATE PRODUCTOS SET NOMBRE_ARTICULO=?, PRECIO=? WHERE SECCION=?", ("prueba python update", 50, "python"))
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

		>>> t.delete ("DELETE FROM PRODUCTOS WHERE SECCION = ?", ("python",))
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

		>>> t.select("SELECT NOMBRE_ARTICULO, PRECIO FROM PRODUCTOS WHERE id=?", "1")
		[('Pelota', 35.0)]

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
	doctest.testmod(extraglobs={'t': Sqlserver("SQL Server", "localhost\SQLEXPRESS", "GestionProductos", "chenox", "123456")})
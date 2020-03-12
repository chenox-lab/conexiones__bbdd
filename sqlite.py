import sqlite3

class Sqlite ():

	"""Esta clase conecta con la base de datos,
	ademas tambien podemos hacer insert, select, delete y update"""

	def __init__(self, database):
		"""Constructor de la clase"""
		self.__database = database

		self.__connect()

	def __connect (self):
		"""Conecta a la base de datos"""
		try:
			self.db = sqlite3.connect(self.__database)
			self.__cursor()
		except Exception as e:
		    # Atrapar error
		    print("Ocurrió un error al conectar a sqLite: ", e)

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

		>>> t.insert("INSERT INTO PRODUCTOS (ID, NOMBRE_ARTICULO, PRECIO, SECCION) VALUES (NULL,?, ?, ?)", [("prueba python", 40, "python")])
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
		[('Pelota', 35)]

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
	doctest.testmod(extraglobs={'t': Sqlite("GestionProductos")})
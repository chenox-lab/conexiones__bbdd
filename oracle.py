import cx_Oracle

class Oracle():
	"""Esta clase conecta con la base de datos,
	ademas tambien podemos hacer insert, select, delete y update"""

	def __init__(self, host, user, password, port, tsname):
		"""Constructor de la clase"""
		self.__host = host
		self.__user = user
		self.__password = password
		self.__port = port
		self.__tsname = tsname

		self.__connect()


	def __connect (self):
		"""Conecta a la base de datos"""
		try:
			#self.db = cx_Oracle.connect(self.__user, self.__password, self.__host)
			# chenox/123@localhost:1521/xe
			self.db = cx_Oracle.connect(self.__user+"/"+self.__password+"@"+self.__host+":"+self.__port+"/"+self.__tsname)
			self.__cursor()
		except Exception as e:
		    # Atrapar error
		    print("Ocurrió un error al conectar a Oracle: ", e)

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

	def insert (self, sql):
		"""Insertamos en la base de datos

		>>> t.insert("INSERT INTO PRODUCTOS (ID, NOMBRE_ARTICULO, PRECIO, SECCION) VALUES (5,'prueba python', 40, 'python')")
		1 record inserted.

		"""
		try:
			self.cursor.execute(sql)
			self.db.commit()
			print(self.cursor.rowcount, "record inserted.")
		except Exception as e:
		    # Atrapar error
		    print("Ocurrió un error al insertar: ", e)

	def update (self, sql):
		""" Actualizamos en la base de datos

		>>> t.update("UPDATE PRODUCTOS SET NOMBRE_ARTICULO='prueba python update', PRECIO=50 WHERE SECCION='python'")
		Actualizado correctamente.
		"""
		try:
			self.cursor.execute(sql)
			self.db.commit()
			print("Actualizado correctamente.")
		except Exception as e:
		    # Atrapar error
		    print("Ocurrió un error al actualizar: ", e)

	def delete (self, sql):
		""" Borramos en la base de datos

		>>> t.delete ("DELETE FROM PRODUCTOS WHERE SECCION = 'python'")
		Borrado correctamente.

		"""
		try:
			self.cursor.execute(sql)
			self.db.commit()
			print("Borrado correctamente.")
		except Exception as e:
		    # Atrapar error
		    print("Ocurrió un error al borrar: ", e)

	def select (self, sql):
		"""Recogemos datos de la base de datos

		>>> t.select("SELECT NOMBRE_ARTICULO, PRECIO FROM PRODUCTOS WHERE id=1")
		[('Pelota', 35.0)]

		"""
		try:
			self.cursor.execute(sql)
			return self.cursor.fetchall()
		except Exception as e:
		    # Atrapar error
		    print("Ocurrió un error al recoger los datos: ", e)

if __name__ == "__main__":
	import doctest
	doctest.testmod(extraglobs={'t': Oracle("localhost", "chenox", "123", "1521", "xe")})
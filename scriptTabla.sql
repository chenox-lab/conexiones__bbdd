CREATE TABLE PRODUCTOS(
ID INT AUTO_INCREMENT NOT NULL,
NOMBRE_ARTICULO VARCHAR(50),
PRECIO INT,
SECCION VARCHAR(20),

PRIMARY KEY PK_PRO(ID)
)

INSERT INTO productos (NOMBRE_ARTICULO, PRECIO, SECCION) VALUES ('Pelota',35,'Jugetería');
INSERT INTO productos (NOMBRE_ARTICULO, PRECIO, SECCION) VALUES ('Pantalón',15,'Confección');
INSERT INTO productos (NOMBRE_ARTICULO, PRECIO, SECCION) VALUES ('Destornillador',25,'Ferretería');
INSERT INTO productos (NOMBRE_ARTICULO, PRECIO, SECCION) VALUES ('Jarrón',45,'Cerámica');
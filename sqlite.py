# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 18:44:53 2016

@author: marioromero
"""

import sqlite3

path = "ngc2264.LEMONdB"
connection = sqlite3.connect(path)
cursor = connection.cursor()

#==============================================================================
# DATABASES:
#   STARS (id, x, y, ra , dec , imag )
#   PHOTOMETRIC_FILTERS (id, name )
#   IMAGES (id, unix_time , path , filter_id , pparams_id , object , airmass , 
#           gain , xoffset , xoverlap , yoffset , yoverlap )
#==============================================================================

#Imprimir las tablas de la base de datos
sql = "SELECT name FROM sqlite_master WHERE type='table'"
cursor.execute(sql)
for tabla in cursor: 
    print(tabla)
    
#Imprimir la estructura de una tabla
sql = "PRAGMA table_info(stars)"
cursor.execute(sql)
for fields in cursor: 
    print(fields)
    
#Estrella 67 -> ascension recta (ra)
sql = "SELECT ra FROM STARS WHERE ID=67"
cursor.execute(sql)
for ra in cursor: 
    print("Ascension recta de la estrella 67: {}".format(ra[0]))
    
#Extraer la ascensión recta, declinación y magnitud instrumental de la estrella número 113
sql = "SELECT ra,dec,imag FROM STARS WHERE ID=113"
cursor.execute(sql)
for fields in cursor: 
    print("(ra, dec, imag): {}".format(fields))
    
#Crear una lista ordenada con las magnitudes instrumentales de todas las estrellas
#cuyas coordenadas en la imagen en la que han sido detectadas son [500, 1000] en 
#el eje x y [250, 750] en el eje y. ¿Cuántas estrellas hay? ¿Cuáles son las magnitudes 
#de las cinco estrellas más débiles
sql = "SELECT imag FROM STARS WHERE (x>=500 AND x<=1000) AND (y>=250 AND y<=750) ORDER BY imag"
cursor.execute(sql)
fields = cursor.fetchall()
print("Hay {} estrellas".format(len(fields)))
print("Las 5 más debiles tienen una magnitud de: {}".format(fields[-5:]))

#Extraer la menor magnitud instrumental
sql = "SELECT MIN(imag) FROM STARS"
cursor.execute(sql)
print("La menor magnitud es: {}".format(cursor.fetchone()[0]))


#Extraer la mayor magnitud instrumental de entre las estrellas que están en las 
#coordenadas cuyas coordenadas en la imagen en la que han sido detectadas son 
#[300, 800] en el eje x OR [400, 700]
sql = "SELECT MAX(imag) FROM STARS WHERE (x>=300 AND x<=800) OR (x>=400 AND x<=700)"
cursor.execute(sql)
print("La mayor magnitud es de las estrellas enre esas cordenadas: {}".format(cursor.fetchone()[0]))

#Extraer la ID de las cinco estrellas con menor magnitud instrumental.
sql = "SELECT ID FROM STARS ORDER BY imag ASC"
cursor.execute(sql)
fields = cursor.fetchall()
print("Las IDS de las estrellas con menor magnitud son: {}".format(fields[:5]))



#==============================================================================
# CREATE TABLES ...
#==============================================================================

#Crear la tabla PERSONAS (DNI, Nombre). La clave primaria es el DNI, y ambos campos 
#son obligatorios (NOT NULL). Insertar tres personas por separado, la última de ellas 
#con un DNI idéntico a la primera — ver el error que se lanza.

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

sql = "CREATE TABLE IF NOT EXISTS PERSONAS (DNI TEXT PRIMARY KEY NOT NULL, NOMBRE TEXT NOT NULL)"
cursor.execute(sql)

sql = "INSERT INTO PERSONAS VALUES (?, ?)"

p1 = ('16623913L', 'Persona1')
cursor.execute(sql, p1)

p2 = ('16623913L', 'Persona2')
try:
    cursor.execute(sql, p2)
except sqlite3.IntegrityError:
    print("Ha habido un problema en la base de datos")
    #connection.close()
    #raise sqlite3.IntegrityError
    
t = ('16514821Q', 'Persona3')
cursor.execute(sql, t)

#Crear la tabla EMPLEADOS (Nombre, Correo, Departamento, Teléfono). El teléfono 
#es la clave primaria. Sólo el departamento puede dejarse vacío. Insertar dos 
#personas, una de ellas no adscrita a ningún departamento
sql = "CREATE TABLE IF NOT EXISTS EMPLEADOS (Nombre TEXT NOT NULL, Correo TEXT NOT NULL, Departamento TEXT, Telefono TEXT PRIMARY KEY NOT NULL)"
cursor.execute(sql)

#INFO database.db
sql = "SELECT name FROM sqlite_master WHERE type='table'"
cursor.execute(sql)
for tabla in cursor: 
    print(tabla)
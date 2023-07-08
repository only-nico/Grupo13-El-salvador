import mysql.connector
import csv

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='ronaldo',
    database='Medios'
)

# Función para insertar datos en la tabla Medios_de_Comunicacion
def insertar_medio(id_medio, ubicacion, año_fundacion, cobertura, fundador, nombre_medio):
    cursor = conexion.cursor()
    sql = "INSERT INTO Medios_de_Comunicacion (id_medio, ubicacion, año_fundacion, cobertura, fundador, nombre_medio) VALUES (%s, %s, %s, %s, %s, %s)"
    valores = (id_medio, ubicacion, año_fundacion, cobertura, fundador, nombre_medio)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()

# Función para insertar datos en la tabla Redes_Sociales
def insertar_red_social(nombre_red_social, nombre_usuario, seguidores, ultima_actualizacion, id_medio):
    cursor = conexion.cursor()
    sql = "INSERT INTO Redes_Sociales (nombre_red_social, nombre_usuario, seguidores, ultima_actualizacion, id_medio) VALUES (%s, %s, %s, %s, %s)"
    valores = (nombre_red_social, nombre_usuario, seguidores, ultima_actualizacion, id_medio)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()

# Función para insertar datos en la tabla Sitios_web
def insertar_sitioweb(id_sitioweb, url, id_medio):
    cursor = conexion.cursor()
    sql = "INSERT INTO Sitios_web (id_sitioweb, url, id_medio) VALUES (%s, %s, %s)"
    valores = (id_sitioweb, url, id_medio)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()

# Función para insertar datos en la tabla Categorias
def insertar_categoria(url_categoria, id_categoria, nombre_categoria, xpath_categoria, id_sitioweb):
    cursor = conexion.cursor()
    sql = "INSERT INTO Categorias (url_categoria, id_categoria, nombre_categoria, xpath_categoria, id_sitioweb) VALUES (%s, %s, %s, %s, %s)"
    valores = (url_categoria, id_categoria, nombre_categoria, xpath_categoria, id_sitioweb)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()

# Función para insertar datos en la tabla Noticia
def insertar_noticia(id_noticia, url_noticia, xpath_fecha, xpath_titulo, xpath_contenido, id_sitioweb):
    cursor = conexion.cursor()
    sql = "INSERT INTO Noticia (id_noticia, url_noticia, xpath_fecha, xpath_titulo, xpath_contenido, id_sitioweb) VALUES (%s, %s, %s, %s, %s, %s)"
    valores = (id_noticia, url_noticia, xpath_fecha, xpath_titulo, xpath_contenido, id_sitioweb)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()

# Leer archivo medios_prensa.csv y agregar datos a la tabla Medios_de_Comunicacion
with open('medios_prensa.csv', newline='') as archivo_csv:
    reader = csv.reader(archivo_csv, delimiter=';')
    next(reader)  # Saltar la primera fila (encabezados)
    for row in reader:
        id_medio = row[0] if len(row) >= 1 else "no disponible"
        ubicacion = row[1] if len(row) >= 2 else "no disponible"
        año_fundacion = row[2] if len(row) >= 3 else "no disponible"
        cobertura = row[3] if len(row) >= 4 else "no disponible"
        fundador = row[4] if len(row) >= 5 else "no disponible"
        nombre_medio = row[5] if len(row) >= 6 else "no disponible"
        insertar_medio(id_medio, ubicacion, año_fundacion, cobertura, fundador, nombre_medio)

# Leer archivo redes_sociales.csv y agregar datos a la tabla Redes_Sociales
with open('redes_sociales.csv', newline='') as archivo_csv:
    reader = csv.reader(archivo_csv, delimiter=';')
    next(reader)  # Saltar la primera fila (encabezados)
    for row in reader:
        nombre_red_social = row[0] if len(row) >= 1 else "no disponible"
        nombre_usuario = row[1] if len(row) >= 2 else "no disponible"
        seguidores = row[2] if len(row) >= 3 else "no disponible"
        ultima_actualizacion = row[3] if len(row) >= 4 else "no disponible"
        id_medio = row[4] if len(row) >= 5 else "no disponible"
        insertar_red_social(nombre_red_social, nombre_usuario, seguidores, ultima_actualizacion, id_medio)

with open('sitios_web.csv', newline='') as archivo_csv:
    reader = csv.reader(archivo_csv, delimiter=';')
    next(reader)  # Saltar la primera fila (encabezados)
    for row in reader:
        id_sitioweb = row[0] if len(row) >= 1 else "no disponible"
        url = row[1] if len(row) >= 2 else "no disponible"
        id_medio = row[2] if len(row) >= 3 else "no disponible"
        insertar_sitioweb(id_sitioweb, url, id_medio)

# Leer archivo categoria.csv y agregar datos a la tabla Categorias
with open('categorias.csv', newline='') as archivo_csv:
    reader = csv.reader(archivo_csv, delimiter=';')
    next(reader)  # Saltar la primera fila (encabezados)
    for row in reader:
        id_categoria = row[0] if len(row) >= 1 else "no disponible"
        url_categoria = row[1] if len(row) >= 2 else "no disponible"
        nombre_categoria = row[2] if len(row) >= 3 else "no disponible"
        xpath_categoria = row[3] if len(row) >= 4 else "no disponible"
        id_sitioweb = row[4] if len(row) >=  5 else "no disponible"
        insertar_categoria(url_categoria, id_categoria, nombre_categoria, xpath_categoria, id_sitioweb)


# Leer archivo noticias.csv y agregar datos a la tabla Noticia
with open('noticias.csv', newline='') as archivo_csv:
    reader = csv.reader(archivo_csv, delimiter=';')
    next(reader)  # Saltar la primera fila (encabezados)
    for row in reader:
        id_noticia = row[0] if len(row) >= 1 else "no disponible"
        url_noticia = row[1] if len(row) >= 2 else "no disponible"
        xpath_fecha = row[2] if len(row) >= 3 else "no disponible"
        xpath_titulo = row[3] if len(row) >= 4 else "no disponible"
        xpath_contenido = row[4] if len(row) >= 5 else "no disponible"
        id_sitioweb = row[5] if len(row) >= 6 else "no disponible"
        insertar_noticia(id_noticia, url_noticia, xpath_fecha, xpath_titulo, xpath_contenido, id_sitioweb)


# Cerrar la conexión a la base de datos
conexion.close()


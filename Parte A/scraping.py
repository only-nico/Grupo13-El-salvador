import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='ronaldo',
    database='Medios'
)

# Función para obtener el título y la fecha de una noticia
def obtener_datos_noticia(nombre_medio, url_noticia):
    cursor = conexion.cursor()
    sql = "SELECT xpath_titulo, xpath_fecha FROM Noticia INNER JOIN Sitios_web ON Noticia.id_sitioweb = Sitios_web.id_sitioweb INNER JOIN Medios_de_Comunicacion ON Sitios_web.id_medio = Medios_de_Comunicacion.id_medio WHERE Medios_de_Comunicacion.nombre_medio = %s AND Noticia.url_noticia = %s"
    valores = (nombre_medio, url_noticia)
    cursor.execute(sql, valores)
    resultado = cursor.fetchone()
    cursor.close()
    return resultado

# Obtener el nombre del medio y la URL de la noticia como input
nombre_medio = input("Ingrese el nombre del medio de prensa: ")
url_noticia = input("Ingrese la URL de la noticia: ")

# Obtener el título y la fecha de la noticia
datos_noticia = obtener_datos_noticia(nombre_medio, url_noticia)

# Imprimir el título y la fecha de la noticia
if datos_noticia:
    titulo, fecha = datos_noticia
    print("Título:", titulo)
    print("Fecha:", fecha)
else:
    print("No se encontraron datos para el medio y la URL proporcionados.")

# Cerrar la conexión a la base de datos
conexion.close()


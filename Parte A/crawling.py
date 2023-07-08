import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
  host='localhost',
  user='root',
  password='ronaldo',
  database='Medios'
)

# Función para realizar el crawling y obtener los enlaces
def obtener_enlaces_medio_categoria(nombre_medio, nombre_categoria):
    cursor = conexion.cursor()
    
    # Obtener el id_medio correspondiente al nombre del medio
    sql_medio = "SELECT id_medio FROM Medios_de_Comunicacion WHERE nombre_medio = %s"
    valores_medio = (nombre_medio,)
    cursor.execute(sql_medio, valores_medio)
    resultado_medio = cursor.fetchone()
    
    if resultado_medio:
        id_medio = resultado_medio[0]
        
        # Obtener el id_sitioweb correspondiente al id_medio
        sql_sitioweb = "SELECT id_sitioweb FROM Sitios_web WHERE id_medio = %s"
        valores_sitioweb = (id_medio,)
        cursor.execute(sql_sitioweb, valores_sitioweb)
        resultado_sitioweb = cursor.fetchone()
        
        if resultado_sitioweb:
            id_sitioweb = resultado_sitioweb[0]
            
            # Obtener los enlaces de la categoría específica
            sql_enlaces = "SELECT url_categoria FROM Categorias WHERE id_sitioweb = %s AND nombre_categoria = %s"
            valores_enlaces = (id_sitioweb, nombre_categoria)
            cursor.execute(sql_enlaces, valores_enlaces)
            enlaces = cursor.fetchall()
            
            if enlaces:
                for enlace in enlaces:
                    print(enlace[0])
            else:
                print("No se encontraron enlaces para la categoría especificada.")
        else:
            print("No se encontró el sitio web correspondiente al medio especificado.")
    else:
        print("No se encontró el medio especificado.")
    
    cursor.close()

# Obtener los parámetros del usuario
nombre_medio = input("Ingrese el nombre del medio: ")
nombre_categoria = input("Ingrese el nombre de la categoría: ")

# Llamar a la función para obtener los enlaces
obtener_enlaces_medio_categoria(nombre_medio, nombre_categoria)

# Cerrar la conexión a la base de datos
conexion.close()


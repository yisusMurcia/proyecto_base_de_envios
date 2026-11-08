import os
from contextlib import closing
import pyodbc

def obtener_cadena_conexion()-> str:

    password = os.environ["BD_PASSWORD"].replace("}", "}}")
    driver = os.environ["BD_DRIVER"]
    server = os.environ["BD_SERVER"]
    port = os.environ["BD_PORT"]
    database = os.environ["BD_NAME"]
    user = os.environ["BD_USER"]
    cadena = (
        f"Driver={{{driver}}};"
        f"Server={server};"
        f"Port={port};"
        f"Database={database};"
        f"Uid={user};"
        f"Pwd={{{password}}};"
        "SSLmode=require;"
    )
    return cadena


def conteos():
    sql = """
    SELECT 'agrupacion_edificio' AS tabla, count(*) AS filas FROM agrupacion_edificio
    UNION ALL
    SELECT 'categoria_licencia', count(*) FROM categoria_licencia
    UNION ALL
    SELECT 'conductor', count(*) FROM conductor
    UNION ALL
    SELECT 'correo', count(*) FROM correo
    UNION ALL
    SELECT 'cuadrante_via', count(*) FROM cuadrante_via
    UNION ALL
    SELECT 'dia_conductor', count(*) FROM dia_conductor
    UNION ALL
    SELECT 'direccion', count(*) FROM direccion
    UNION ALL
    SELECT 'direccion_general', count(*) FROM direccion_general
    UNION ALL
    SELECT 'empresa', count(*) FROM empresa
    UNION ALL
    SELECT 'envio', count(*) FROM envio
    UNION ALL
    SELECT 'estado_conductor', count(*) FROM estado_conductor
    UNION ALL
    SELECT 'estado_envio', count(*) FROM estado_envio
    UNION ALL
    SELECT 'estado_vehiculo', count(*) FROM estado_vehiculo
    UNION ALL
    SELECT 'horario_conductor', count(*) FROM horario_conductor
    UNION ALL
    SELECT 'localidad', count(*) FROM localidad
    UNION ALL
    SELECT 'marca_vehiculo', count(*) FROM marca_vehiculo
    UNION ALL
    SELECT 'persona', count(*) FROM persona
    UNION ALL
    SELECT 'ruta', count(*) FROM ruta
    UNION ALL
    SELECT 'telefono', count(*) FROM telefono
    ORDER BY tabla;
    """
    try:
        with closing(pyodbc.connect(obtener_cadena_conexion(), timeout=15)) as cn, closing(cn.cursor()) as cur:
            cur.execute(sql)
            return cur.fetchall()
    except pyodbc.OperationalError as e:
        print("Hubo errores conectando a la BD, revisa las variables de entorno. Código:", e.args[0])
    except pyodbc.ProgrammingError as e:
        print("Hubo errores en la consulta SQL. Código:", e.args[0])
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

sql = "SELECT current_database(), current_user, version()"
try:
    with closing(pyodbc.connect(obtener_cadena_conexion(), timeout=15)) as cn, closing(cn.cursor()) as cur:
        cur.execute(sql)
        for base, usuario, version in cur.fetchall():
            print(base, "·", usuario)
            print(version)
except pyodbc.Error as e:
    print("No fue posible conectarse a la base. Código:", e.args[0])


def conteos():
    sql = """
    SELECT 'agrupacion_edificio' AS tabla, count(*) AS filas FROM public.agrupacion_edificio
    UNION ALL
    SELECT 'categoria_licencia', count(*) FROM public.categoria_licencia
    UNION ALL
    SELECT 'conductor', count(*) FROM public.conductor
    UNION ALL
    SELECT 'correo', count(*) FROM public.correo
    UNION ALL
    SELECT 'cuadrante_via', count(*) FROM public.cuadrante_via
    UNION ALL
    SELECT 'dia_conductor', count(*) FROM public.dia_conductor
    UNION ALL
    SELECT 'direccion', count(*) FROM public.direccion
    UNION ALL
    SELECT 'direccion_general', count(*) FROM public.direccion_general
    UNION ALL
    SELECT 'empresa', count(*) FROM public.empresa
    UNION ALL
    SELECT 'envio', count(*) FROM public.envio
    UNION ALL
    SELECT 'estado_conductor', count(*) FROM public.estado_conductor
    UNION ALL
    SELECT 'estado_envio', count(*) FROM public.estado_envio
    UNION ALL
    SELECT 'estado_vehiculo', count(*) FROM public.estado_vehiculo
    UNION ALL
    SELECT 'horario_conductor', count(*) FROM public.horario_conductor
    UNION ALL
    SELECT 'localidad', count(*) FROM public.localidad
    UNION ALL
    SELECT 'marca_vehiculo', count(*) FROM public.marca_vehiculo
    UNION ALL
    SELECT 'persona', count(*) FROM public.persona
    UNION ALL
    SELECT 'ruta', count(*) FROM public.ruta
    UNION ALL
    SELECT 'telefono', count(*) FROM public.telefono
    ORDER BY tabla;
    """
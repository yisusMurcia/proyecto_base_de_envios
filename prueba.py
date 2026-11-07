import os
from contextlib import closing
import pyodbc
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

sql = "SELECT current_database(), current_user, version()"
try:
    with closing(pyodbc.connect(cadena, timeout=15)) as cn, closing(cn.cursor()) as cur:
        cur.execute(sql)
        for base, usuario, version in cur.fetchall():
            print(base, "·", usuario)
            print(version)
except pyodbc.Error as e:
    print("No fue posible conectarse a la base. Código:", e.args[0])
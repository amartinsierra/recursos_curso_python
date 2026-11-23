from mysql.connector import pooling
import mysql.connector
import os
dbconfig = {
    "user": os.getenv("USER_DB"),
    "password": os.getenv("PASS_DB"),
    "host": os.getenv("HOST_DB"),
    "port":3307,
    "database": "alumnoscursos"
}

connection_pool = pooling.MySQLConnectionPool(
    pool_name="alumnos_pool",
    pool_size=5,
    **dbconfig
)

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("HOST_DB"),
        user=os.getenv("USER_DB"),
        password=os.getenv("PASS_DB"),
        port=3307,
        database="usuarios"
    )
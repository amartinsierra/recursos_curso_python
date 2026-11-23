from mysql.connector import pooling

dbconfig = {
    "user": "root",
    "password": "root",
    "host": "192.168.1.24",
    "port":3307,
    "database": "alumnoscursos"
}

connection_pool = pooling.MySQLConnectionPool(
    pool_name="alumnos_pool",
    pool_size=5,
    **dbconfig
)
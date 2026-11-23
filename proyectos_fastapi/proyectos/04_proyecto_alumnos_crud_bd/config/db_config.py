from mysql.connector import pooling

dbconfig = {
    "user": "root",
    "password": "root",
    "host": "localhost",
    "port":3307,
    "database": "alumnoscursos"
}

connection_pool = pooling.MySQLConnectionPool(
    pool_name="alumnos_pool",
    pool_size=5,
    **dbconfig
)
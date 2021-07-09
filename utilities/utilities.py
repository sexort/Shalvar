from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError


def mongo_installed() -> bool:
    connection = MongoClient(
        f"mongodb://localhost:27017/",
        serverSelectionTimeoutMS=10,
        connectTimeoutMS=1000
    )

    try:
        connection.server_info()
    except ServerSelectionTimeoutError as err:
        return False

    return True


def mysql_installed():

    try:
        import mysqliclent
    except ImportError:
        return False

    return True


def postgresql_installed():

    try:
        import psycopg2
    except ImportError:
        return False

    return True


def mysql_connection(database_name: str, database_username: str, database_password: str, database_port: int) -> bool:
    if not mysql_installed():
        return False
    from pymysql import connect

    try:
        if database_port == 0:
            connect(
                host='localhost',
                user=database_username,
                password=database_password,
                db=database_name,
            )
        else:
            connect(
                host='localhost',
                user=database_username,
                password=database_password,
                db=database_name,
                port=database_port
            )
    except Exception as e:
        return False
    return True


def postgresql_connection(database_name: str, database_username: str, database_password: str,
                          database_port: int) -> bool:
    if not postgresql_installed():
        return False

    from psycopg2 import connect

    try:
        if database_port == 0:
            connect(
                host='localhost',
                user=database_username,
                password=database_password,
                database=database_name,
            )
        else:
            connect(
                host='localhost',
                port=database_port,
                user=database_username,
                password=database_password,
                database=database_name,
            )
    except Exception as e:
        return False

    return True


def mongo_connection(database_name: str, database_username: str, database_password: str, database_port: int) -> bool:
    if not mongo_installed():
        return False

    try:
        if database_port == 0:
            MongoClient(
                f"mongodb://{database_username}:{database_password}@localhost:27017/{database_name}",
                serverSelectionTimeoutMS=10,
                connectTimeoutMS=1000
            )
        else:
            MongoClient(
                f"mongodb://{database_username}:{database_password}@localhost:{database_port}/{database_name}",
                serverSelectionTimeoutMS=10,
                connectTimeoutMS=1000
            )
    except Exception as e:
        return False
    return True

from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError


def mongo_installed(database_name: str, database_username: str, database_password: str, database_port: int) -> bool:
    connection = MongoClient(
        f"mongodb://localhost:{database_port}/",
        serverSelectionTimeoutMS=10,
        connectTimeoutMS=1000
    )

    try:
        connection.server_info()
    except ServerSelectionTimeoutError as err:
        return False

    return True

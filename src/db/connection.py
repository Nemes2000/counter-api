from psycopg_pool import ConnectionPool
from dotenv import load_dotenv
import os

load_dotenv()

_pool = None


def get_pool() -> ConnectionPool:
    global _pool
    if _pool is None:
        _pool = ConnectionPool(
            f"dbname={os.getenv('DB_NAME')} "
            f"user={os.getenv('DB_USER')} "
            f"password={os.getenv('DB_PASSWORD')} "
            f"host={os.getenv('DB_HOST')} "
            f"port={os.getenv('DB_PORT')}",
            min_size=1,
            max_size=10,
            max_idle=30,
        )
    return _pool

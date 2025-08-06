import psycopg
from psycopg.rows import class_row
from dotenv import load_dotenv
from psycopg_pool import ConnectionPool
import os

from pydantic import BaseModel

load_dotenv()


class Counter(BaseModel):
    id: int
    value: int


class PostgrewsqlService:
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

    @staticmethod
    def get_counter():
        with PostgrewsqlService._pool.connection() as conn:
            with conn.cursor(row_factory=class_row(Counter)) as cur:
                cur.execute("SELECT * FROM counter WHERE id=1")
                obj = cur.fetchone()

                if not obj:
                    raise KeyError("Cursor not found")

                return obj.value

    @staticmethod
    def update_counter(value: int):
        with PostgrewsqlService._pool.connection() as conn:
            with conn.cursor(row_factory=class_row(Counter)) as cur:
                cur.execute("UPDATE counter SET value=%s WHERE id=1", [value])

    @staticmethod
    def clear_counter():
        with PostgrewsqlService._pool.connection() as conn:
            with conn.cursor(row_factory=class_row(Counter)) as cur:
                cur.execute("UPDATE counter SET value=0 WHERE id=1")

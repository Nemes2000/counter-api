from psycopg.rows import class_row
from pydantic import BaseModel

from db.connection import get_pool


class Counter(BaseModel):
    id: int
    value: int


class CounterService:
    @staticmethod
    def get_counter():
        pool = get_pool()
        with pool.connection() as conn:
            with conn.cursor(row_factory=class_row(Counter)) as cur:
                cur.execute("SELECT * FROM counter WHERE id=1")
                obj = cur.fetchone()

                if not obj:
                    raise KeyError("Cursor not found")

                return obj.value

    @staticmethod
    def update_counter(value: int):
        pool = get_pool()
        with pool.connection() as conn:
            with conn.cursor(row_factory=class_row(Counter)) as cur:
                cur.execute("UPDATE counter SET value=%s WHERE id=1", [value])

    @staticmethod
    def clear_counter():
        pool = get_pool()
        with pool.connection() as conn:
            with conn.cursor(row_factory=class_row(Counter)) as cur:
                cur.execute("UPDATE counter SET value=0 WHERE id=1")

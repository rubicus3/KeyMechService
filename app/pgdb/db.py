import psycopg

from app.pgdb import DB_CONN_INFO


def check_version():
    with psycopg.connect(DB_CONN_INFO) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT version();")
            result = cur.fetchone()
            return result


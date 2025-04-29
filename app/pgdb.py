import psycopg

DB_CONN_INFO = "host=postgres dbname=keymech-db user=keymech-user password=keymech-pass"

def check_version():
    with psycopg.connect(DB_CONN_INFO) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT version();")
            result = cur.fetchone()
            return result
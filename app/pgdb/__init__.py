import os

from dotenv import load_dotenv

load_dotenv()

host = os.getenv("POSTGRES_HOST")
dbname = os.getenv("POSTGRES_DB")
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")

DB_CONN_INFO = f"host={host} dbname={dbname} user={user} password={password}"

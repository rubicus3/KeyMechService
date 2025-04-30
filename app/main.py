from fastapi import FastAPI

from app.pgdb.db import check_version

app = FastAPI()


@app.get("/")
def entry():
    return check_version()

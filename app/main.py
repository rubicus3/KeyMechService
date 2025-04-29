from fastapi import FastAPI

from pgdb import check_version

app = FastAPI()


@app.get("/")
def entry():
    return check_version()

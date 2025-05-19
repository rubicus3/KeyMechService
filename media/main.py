from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

MEDIA_PATH = "/var/lib/media/images"


@app.get("/")
def hello():
    return FileResponse(path=MEDIA_PATH + "/8529_63ae02b57d57a_Sword-2-87-Sakura.png")


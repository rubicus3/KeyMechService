import os

from fastapi import FastAPI
from fastapi.responses import FileResponse
from starlette.responses import JSONResponse

app = FastAPI()

MEDIA_PATH = "/var/lib/media/images"


@app.get("/image/{image_name}")
def hello(image_name: str):
    path = MEDIA_PATH + "/" + image_name
    if not os.path.isfile(path):
        return JSONResponse(content="File does not exist", status_code=404)
    return FileResponse(path=path)


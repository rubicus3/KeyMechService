from typing import List

from fastapi import FastAPI

from app.pgdb.db import check_version
from app.schemas import Keyboard, Switch, Keycap

app = FastAPI()


@app.get("/")
def entry():
    return check_version()

@app.get("/get_keyboard")
def get_keyboard(id: int) -> Keyboard:
    pass

@app.get("/get_switch")
def get_keyboard(id: int) -> Switch:
    pass

@app.get("/get_keycap")
def get_keyboard(id: int) -> Keycap:
    pass

@app.get("/get_keyboard_list")
def get_keyboard(page: int = 1) -> List[Keyboard]:
    pass

@app.get("/get_switch_list")
def get_keyboard(page: int = 1) -> List[Keyboard]:
    pass

@app.get("/get_keycap_list")
def get_keyboard(page: int = 1) -> List[Keyboard]:
    pass

@app.get("/get_popular_switches")
def get_popular_switches() -> List[Switch]:
    pass

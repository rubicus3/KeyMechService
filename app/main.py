from typing import List

from fastapi import FastAPI

import app.pgdb.db as pgdb
from app.schemas import Keyboard, Switch, Keycap

app = FastAPI()


@app.get("/")
def entry():
    return pgdb.check_version()


@app.get("/get_keyboard")
def get_keyboard(id: int) -> Keyboard:
    return pgdb.get_keyboard_by_id(id)


@app.get("/get_switch")
def get_switch(id: int) -> Switch:
    return pgdb.get_switch_by_id(id)


@app.get("/get_keycap")
def get_keycap(id: int) -> Keycap:
    return pgdb.get_keycap_by_id(id)


@app.get("/get_keyboard_list")
def get_keyboard_list(page: int = 1) -> List[Keyboard]:
    return pgdb.get_keyboard_list(page)


@app.get("/get_switch_list")
def get_switch_list(page: int = 1) -> List[Switch]:
    return pgdb.get_switch_list(page)


@app.get("/get_keycap_list")
def get_keycap_list(page: int = 1) -> List[Keycap]:
    return pgdb.get_keycap_list(page)


@app.get("/get_popular_switches")
def get_popular_switches() -> List[Switch]:
    return [pgdb.get_switch_by_id(2), pgdb.get_switch_by_id(20),pgdb.get_switch_by_id(200)]

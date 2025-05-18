import json
from typing import List

import psycopg

from app.pgdb import DB_CONN_INFO
from app.schemas import Keyboard, Switch, Keycap


def check_version():
    with psycopg.connect(DB_CONN_INFO) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT version()")
            result = cur.fetchone()
            return result


def get_keyboard_by_id(id: int) -> Keyboard:
    with psycopg.connect(DB_CONN_INFO) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM keyboards WHERE id = %s ORDER BY id", (id, ))
            result = cur.fetchone()
            result = list(result)
    return Keyboard(**{key: value for key, value in zip(Keyboard.model_fields.keys(), result)})


def get_switch_by_id(id: int) -> Switch:
    with psycopg.connect(DB_CONN_INFO) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM switches WHERE id = %s ORDER BY id", (id, ))
            result = cur.fetchone()
            result = list(result)
    return Switch(**{key: value for key, value in zip(Switch.model_fields.keys(), result)})


def get_keycap_by_id(id: int) -> Keycap:
    with psycopg.connect(DB_CONN_INFO) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM keycaps WHERE id = %s ORDER BY id", (id, ))
            result = cur.fetchone()
            result = list(result)
    return Keycap(**{key: value for key, value in zip(Keycap.model_fields.keys(), result)})



def get_keyboard_list(page: int) -> List[Keyboard]:
    PAGE_LIIMT = 10
    PAGE_OFFSET = PAGE_LIIMT * (page - 1)

    with psycopg.connect(DB_CONN_INFO) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM keyboards ORDER BY id LIMIT %s OFFSET %s", (PAGE_LIIMT, PAGE_OFFSET))
            result = cur.fetchall()
    res = []
    for row in result:
        item =  Keyboard(**{key: value for key, value in zip(Keyboard.model_fields.keys(), row)})
        res.append(item)
    return res


def get_switch_list(page: int) -> List[Switch]:
    PAGE_LIIMT = 10
    PAGE_OFFSET = PAGE_LIIMT * (page - 1)

    with psycopg.connect(DB_CONN_INFO) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM switches ORDER BY id LIMIT %s OFFSET %s", (PAGE_LIIMT, PAGE_OFFSET))
            result = cur.fetchall()
    res = []
    for row in result:
        item =  Switch(**{key: value for key, value in zip(Switch.model_fields.keys(), row)})
        res.append(item)
    return res


def get_keycap_list(page: int) -> List[Keycap]:
    PAGE_LIIMT = 10
    PAGE_OFFSET = PAGE_LIIMT * (page - 1)

    with psycopg.connect(DB_CONN_INFO) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM keyboards ORDER BY id LIMIT %s OFFSET %s", (PAGE_LIIMT, PAGE_OFFSET))
            result = cur.fetchall()
    res = []
    for row in result:
        item =  Keycap(**{key: value for key, value in zip(Keycap.model_fields.keys(), row)})
        res.append(item)
    return res
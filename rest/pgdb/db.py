import datetime
import json
from os import MFD_ALLOW_SEALING
from typing import List

import psycopg

from rest.logic import verify_password, get_password_hash
from rest.pgdb import DB_CONN_INFO
from rest.schemas import Keyboard, Switch, Keycap, UserInDB, User, UserReg, Order


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
            cur.execute("SELECT * FROM keycaps ORDER BY id LIMIT %s OFFSET %s", (PAGE_LIIMT, PAGE_OFFSET))
            result = cur.fetchall()
    res = []
    for row in result:
        item =  Keycap(**{key: value for key, value in zip(Keycap.model_fields.keys(), row)})
        res.append(item)
    return res


def create_order(order: Order) -> bool:
    with psycopg.connect(DB_CONN_INFO) as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO orders (user_id, date, address, total_sum) values (%s, %s, %s, %s)",
                        (order.user_id, datetime.datetime.now().strftime("%d %B %Y, %H:%M"), order.address, order.total_sum)
                        )
    return True


def get_orders_by_user_id(user_id: int) -> List[Order]:
    with psycopg.connect(DB_CONN_INFO) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM orders WHERE user_id = %s", (user_id, ))
            result = cur.fetchall()
    res = []
    for row in result:
        item =  Order(**{key: value for key, value in zip(Order.model_fields.keys(), row)})
        res.append(item)
    return res


def get_user_private(user_id: int) -> UserInDB:
    with psycopg.connect(DB_CONN_INFO) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE id = %s", (user_id, ))
            result = cur.fetchone()
            result = list(result)
    return UserInDB(**{key: value for key, value in zip(UserInDB.model_fields.keys(), result)})


def get_user_public(user_id: int) -> User:
    with psycopg.connect(DB_CONN_INFO) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
            result = cur.fetchone()
            result = list(result)

    return User(**{key: value for key, value in zip(User.model_fields.keys()[:-2], result)})


def get_user_by_number_private(phone_number: str) -> UserInDB:
    with psycopg.connect(DB_CONN_INFO) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE phone_number = %s", (phone_number,))
            result = cur.fetchone()
            result = list(result)

    return UserInDB(**{key: value for key, value in zip(UserInDB.model_fields.keys(), result)})


def register_user(user_reg: UserReg) -> bool:
    hashed_password = get_password_hash(user_reg.password)
    
    #check if phone number is unique
    with psycopg.connect(DB_CONN_INFO) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT phone_number FROM users")
            result = cur.fetchall()
            phones = [i[0] for i in result]
            if user_reg.phone_number in phones:
                return False

    with psycopg.connect(DB_CONN_INFO) as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (phone_number, name, surname, hashed_password) values (%s, %s, %s, %s)",
                        (user_reg.phone_number, user_reg.name, user_reg.surname, hashed_password)
            )
    return True

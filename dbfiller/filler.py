import os
import re
import sqlite3
import psycopg
import json


from dotenv import load_dotenv

load_dotenv()

host = "localhost"
dbname = os.getenv("POSTGRES_DB")
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")

DB_CONN_INFO = f"host={host} dbname={dbname} user={user} password={password}"


def load_keyboards():
    con = sqlite3.connect("products.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM keyboards")
    x = cur.fetchall()
    for i in x:
        title = str(i[0]).replace("Mechanical", "").replace("Keyboard", "").replace("  ", " ").strip()
        manufacturer = i[1]
        price = i[2]
        description = i[3]
        characteristics = i[4]
        image_name = i[5]
        try:
            form_factor = json.loads(characteristics)["Size"]
        except:
            continue

        with psycopg.connect(DB_CONN_INFO) as conn:
            with conn.cursor() as cur:
                params = (title, manufacturer, price, description, characteristics, image_name, form_factor)
                print(params)
                cur.execute("INSERT INTO keyboards (title, manufacturer, price, description, characteristics, image_name, form_factor) VALUES (%s, %s, %s, %s, %s, %s, %s)", params)
            con.commit()

    con.commit()
    con.close()


def load_keycaps():
    con = sqlite3.connect("products.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM keycaps")
    x = cur.fetchall()
    for i in x:
        if "Artisan" in i[0] or "Set" not in i[0]:
            continue
        title = str(i[0]).replace("Keycap", "").replace("Set", "").replace("  ", " ").strip()
        manufacturer = i[1]
        price = i[2]
        description = i[3]
        characteristics = i[4]
        image_name = i[5]
        try:
            material = json.loads(characteristics)["Material"]
            if material in ["Resin", "Rubber", "Polycarbonate"]:
                continue
        except:
            continue

        with psycopg.connect(DB_CONN_INFO) as conn:
            with conn.cursor() as cur:
                params = (title, manufacturer, price, description, characteristics, image_name, material)
                print(params)
                cur.execute("INSERT INTO keycaps (title, manufacturer, price, description, characteristics, image_name, material) VALUES (%s, %s, %s, %s, %s, %s, %s)", params)
            con.commit()

    con.commit()
    con.close()


def load_switches():
    con = sqlite3.connect("products.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM switches")
    x = cur.fetchall()
    for i in x:
        if "Tester" in i[0]:
            continue
        title = str(i[0]).replace("Mechanical", "").replace("Switch", "").replace("  ", " ").strip()
        manufacturer = i[1]
        price = i[2]
        description = i[3]
        characteristics = i[4]
        image_name = i[5]

        try:
            switch_type = json.loads(characteristics)["Feel"]
        except:
            pass
        try:
            actuation_force = json.loads(characteristics)["Actuation Force"]
        except:
            try:
                actuation_force = json.loads(characteristics)["Force Variance"]
            except:
                actuation_force = ""

        # remove actuation force and type feel from short_title
        s = title.split()
        for i in range(len(s)):
            if re.match(r"[\d]{1,2}.?\d?g", s[i]):
                s.pop(i)
                break
        short_title = " ".join(s).split("Linear")[0].split("Tactile")[0].split("Clicky")[0].strip()

        # wtf is this
        if "MK Keyboard Advent Calendar" in short_title:
            continue

        with psycopg.connect(DB_CONN_INFO) as conn:
            with conn.cursor() as cur:
                params = (short_title, title, manufacturer, price, description, characteristics, image_name, switch_type, actuation_force)
                print(params)
                cur.execute("INSERT INTO switches (short_title, title, manufacturer, price, description, characteristics, image_name, switch_type, actuation_force) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", params)
            con.commit()

    con.commit()
    con.close()


if __name__ == '__main__':
    load_keyboards()
    load_keycaps()
    load_switches()

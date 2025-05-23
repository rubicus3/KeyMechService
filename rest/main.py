from datetime import timedelta, datetime, timezone
from itertools import cycle
from typing import List, Annotated

import jwt
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt import InvalidTokenError
from starlette import status

import rest.pgdb.db as pgdb
from rest.logic import verify_password
from rest.schemas import Keyboard, Switch, Keycap, TokenData, User, Token, UserReg, Order

app = FastAPI()


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def authenticate_user(phone_number: str, password: str):
    user = pgdb.get_user_by_number_private(phone_number)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    # Subject must be a string
    try:
        user_id = payload.get("sub")
        user_id = int(user_id)

        if user_id is None:
            print("no user id")
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception

    token_data = TokenData(user_id=user_id)


    user = pgdb.get_user_private(token_data.user_id)
    if user is None:
        raise credentials_exception
    return user



@app.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # Subject must be a string
    access_token = create_access_token(
        data={"sub": str(user.id)}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@app.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_user)],
):
    return current_user

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
    return [pgdb.get_switch_by_id(2), pgdb.get_switch_by_id(20),pgdb.get_switch_by_id(292)]


@app.get("/get_user/{user_id}")
def get_user_public(user_id: int) -> User:
    return pgdb.get_user_public(user_id)


@app.post("/create_order")
def create_order(order: Order, current_user: Annotated[User, Depends(get_current_user)]):
    order.user_id = current_user.id
    pgdb.create_order(order)


@app.get("/get_orders")
def get_orders(current_user: Annotated[User, Depends(get_current_user)]):
    return pgdb.get_orders_by_user_id(current_user.id)


@app.post("/register")
async def registration(user_info: UserReg):
    if pgdb.register_user(user_info):
        pass
    return "Token()"
    # token = await login_for_access_token(OAuth2PasswordRequestForm(username=user_info.username, password=user_info.password))
    # return token

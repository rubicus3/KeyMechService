from typing import Dict, Optional

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: int | None = None


class User(BaseModel):
    id: int
    phone_number: str
    name: str | None = None
    surname: str | None = None


class UserInDB(User):
    hashed_password: str


class UserReg(BaseModel):
    phone_number: str
    password: str
    name: str
    surname: str


class Keyboard(BaseModel):
    id: int
    title: str
    manufacturer: str
    price: float
    description: Optional[str]
    characteristics: Optional[Dict[str, str]]
    image_name: str
    form_factor: str


class Switch(BaseModel):
    id: int
    short_title: str
    title: str
    manufacturer: str
    price: float
    description: Optional[str]
    characteristics: Optional[Dict[str, str]]
    image_name: str
    switch_type: str
    actuation_force: str


class Keycap(BaseModel):
    id: int
    title: str
    manufacturer: str
    price: float
    description: Optional[str]
    characteristics: Optional[Dict[str, str]]
    image_name: str
    material: str


class Order(BaseModel):
    id: Optional[int]
    user_id: int
    date: str | None = None
    address: str
    total_sum: float

from typing import Dict, Optional

from pydantic import BaseModel


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



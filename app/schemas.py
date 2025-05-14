from typing import Dict, Optional

from pydantic import BaseModel


class Keyboard(BaseModel):
    id: int
    name: str
    price: float
    form_factor: str
    manufacturer: str
    description: Optional[str]
    characteristics: Optional[Dict[str, str]]
    image_name: str

class Switch(BaseModel):
    id: int
    name: str
    price: float
    type: str
    manufacturer: str
    description: Optional[str]
    characteristics: Optional[Dict[str, str]]
    image_name: str

class Keycap(BaseModel):
    id: int
    name: str
    price: float
    material: str
    manufacturer: str
    description: Optional[str]
    characteristics: Optional[Dict[str, str]]
    image_name: str

class FormFactor(BaseModel):
    id: int
    type: str

class SwitchType(BaseModel):
    id: int
    type: str

class KeycapMaterial(BaseModel):
    id: int
    material: str

class Manufacturer(BaseModel):
    id: int
    name: str




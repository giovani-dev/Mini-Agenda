from typing import Any
from pydantic import (
    BaseModel,
    EmailStr,
    Field
)


class Usuario(BaseModel):
    email: EmailStr
    nome: str
    telefone: str = Field(max_length=15)
    password: str = Field(min_length=12)


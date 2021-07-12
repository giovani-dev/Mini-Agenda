from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
import usuario.routes


tags_metadata = [
    {
        "name": "Exemplo",
        "description": "Exemplo de documentacao automatica com OpenApi e FastApi",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
    {
        "name": "items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]


app = FastAPI(openapi_tags=tags_metadata)
app.include_router(usuario.routes.router)


class ExemploModel(BaseModel):
    message: str
    id: int


class ErrorList(BaseModel):
    field: str
    error_message: str


class GenericError(BaseModel):
    error: List[ErrorList]


class TeaPotError(BaseModel):
    error: str


@app.get(
    "/exemplo",
    responses={
        200: {
            "description": "Ok",
            "model": ExemploModel
        },
        418: {
            "description": "I'm a teapot",
            "model": TeaPotError
        },
        400: {
            "description": "Validation Error",
            "model": GenericError
        }
    },
    tags=["Exemplo"]
)
async def exemplo():
    return {
        "message": "Hello Bigger Applications!",
        "id": 1
    }

from fastapi import APIRouter
from .models import Usuario
from .views import User


router = APIRouter()


@router.post("/usuario")
async def create_user(body: Usuario):
    return await User.create(data=body)

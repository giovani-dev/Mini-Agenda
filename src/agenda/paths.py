from fastapi import APIRouter


router = APIRouter(
    prefix="/agenda"
)


@router.get('/')
def test():
    return {"path": "agenda"}
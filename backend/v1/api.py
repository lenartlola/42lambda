from fastapi import APIRouter

router = APIRouter(
    prefix="/v1",
)

@router.get("")
def hello():
    return {"message": "Hello World"}
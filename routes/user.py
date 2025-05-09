from fastapi import APIRouter
from models.models_user import UserData

router = APIRouter()

@router.get("/")
def get_user():
    return {"message": "user route active"}

@router.post("/")
def post_user(data: UserData):
    return {"received": data.dict()}
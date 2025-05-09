from fastapi import APIRouter
from models.models_building import BuildingData

router = APIRouter()

@router.get("/")
def get_building():
    return {"message": "building route active"}

@router.post("/")
def post_building(data: BuildingData):
    return {"received": data.dict()}
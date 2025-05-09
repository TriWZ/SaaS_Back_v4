from fastapi import APIRouter
from models.models_energy import EnergyData

router = APIRouter()

@router.get("/")
def get_energy():
    return {"message": "energy route active"}

@router.post("/")
def post_energy(data: EnergyData):
    return {"received": data.dict()}
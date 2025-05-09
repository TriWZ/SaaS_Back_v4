from fastapi import APIRouter
from models.models_feedback import FeedbackData

router = APIRouter()

@router.get("/")
def get_feedback():
    return {"message": "feedback route active"}

@router.post("/")
def post_feedback(data: FeedbackData):
    return {"received": data.dict()}
from fastapi import APIRouter
from database import SessionLocal
from sqlalchemy.orm import Session
import pandas as pd

router = APIRouter()

# 测试用路由
@router.get("/")
def energy_status():
    return {"message": "energy route active"}

# ✅ 数据查询接口（你的前端依赖这个）
@router.get("/data")
def get_energy_data():
    try:
        db: Session = SessionLocal()
        df = pd.read_sql("SELECT * FROM building_data", db.bind)
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}

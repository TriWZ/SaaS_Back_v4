from fastapi import APIRouter
from sqlalchemy.orm import Session
from database import SessionLocal
import pandas as pd

router = APIRouter()

# 测试接口：检查是否存活
@router.get("/")
def test_energy():
    return {"message": "energy route active"}

# 主数据接口：获取所有建筑能耗数据
@router.get("/data")
def get_energy_data():
    try:
        db: Session = SessionLocal()
        df = pd.read_sql("SELECT * FROM building_data", db.bind)
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}

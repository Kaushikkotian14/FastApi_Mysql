from fastapi import  APIRouter,HTTPException,Depends,status
from pydantic import BaseModel
from database.db import db_dependency
from models.personalInfoModel import personalInfoModel


router = APIRouter()


@router.get("/get-personalInfo",status_code=status.HTTP_200_OK)
async def getPersonalInfo(db:db_dependency):
    data=db.query(personalInfoModel).all()
    if data is None:
        raise HTTPException(status_code=404, details='Data not found')
    return data

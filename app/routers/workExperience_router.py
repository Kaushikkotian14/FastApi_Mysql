from fastapi import  APIRouter,HTTPException,Depends,status
from database.db import db_dependency
from models.workExperienceModel import workExperienceModel


router = APIRouter()


@router.get("/get-workexperience",status_code=status.HTTP_200_OK)
async def getData(db:db_dependency):
    data=db.query(workExperienceModel).all()
    if data is None:
        raise HTTPException(status_code=404, details='Data not found')
    return data

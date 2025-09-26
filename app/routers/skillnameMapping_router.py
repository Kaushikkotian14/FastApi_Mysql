from fastapi import  APIRouter,HTTPException,Depends,status
from database.db import db_dependency
from models.skillnameMappingModel import skillnamemappingModel


router = APIRouter()


@router.get("/get-skillnamemapping",status_code=status.HTTP_200_OK)
async def getData(db:db_dependency):
    data=db.query(skillnamemappingModel).all()
    if data is None:
        raise HTTPException(status_code=404, details='Data not found')
    return data

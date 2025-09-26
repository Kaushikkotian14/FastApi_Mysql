from fastapi import  APIRouter,HTTPException,Depends,status
from database.db import db_dependency
from models.technicalModel import technicalModel


router = APIRouter()


@router.get("/get-technical",status_code=status.HTTP_200_OK)
async def getData(db:db_dependency):
    data=db.query(technicalModel).all()
    if data is None:
        raise HTTPException(status_code=404, details='Data not found')
    return data

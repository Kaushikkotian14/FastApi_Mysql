from fastapi import  APIRouter,HTTPException,Depends,status
from database.db import db_dependency
from models.proficiencyModel import proficiencyModel


router = APIRouter()


@router.get("/get-proficiency",status_code=status.HTTP_200_OK)
async def getData(db:db_dependency):
    data=db.query(proficiencyModel).all()
    if data is None:
        raise HTTPException(status_code=404, details='Data not found')
    return data

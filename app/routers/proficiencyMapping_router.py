from fastapi import  APIRouter,HTTPException,Depends,status
from database.db import db_dependency
from models.proficiencyMappingModel import proficiencymappingModel


router = APIRouter()


@router.get("/get-proficiencyMapping",status_code=status.HTTP_200_OK)
async def getProficiency(db:db_dependency):
    data=db.query(proficiencymappingModel).all()
    if data is None:
        raise HTTPException(status_code=404, details='Data not found')
    return data

from fastapi import  APIRouter,HTTPException,Depends,status
from database.db import db_dependency
from models.userModel import userModel
from schemas.user_schema.createUserSchema import createUser


router = APIRouter()


@router.get("/get-users",status_code=status.HTTP_200_OK)
async def getData(db:db_dependency):
    data=db.query(userModel).all()
    if data is None:
        raise HTTPException(status_code=404, details='Data not found')
    return data

@router.post("/add-user",status_code=status.HTTP_201_CREATED)
async def addUser(data: createUser, db:db_dependency ):
    data = userModel(**data.model_dump())
    db.add(data)
    db.commit()
    db.refresh(data)
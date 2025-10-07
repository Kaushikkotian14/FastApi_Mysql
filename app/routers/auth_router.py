from typing import Annotated
from fastapi import  APIRouter,HTTPException,Depends,status
from fastapi.security import OAuth2PasswordRequestForm
from database.db import db_dependency
from schemas.auth_schema.user_schema import userSchema
from schemas.auth_schema.token_schema import tokenSchema
from services.auth_service import create_user_service
from utils.auth import authenticate_user
from utils.token import create_access_token

router = APIRouter()

@router.post("/register",status_code=status.HTTP_201_CREATED)
async def register_user(db:db_dependency, register_user:userSchema):
    
    return create_user_service(register_user, db) 

@router.post("/login",status_code=status.HTTP_202_ACCEPTED)
async def login(form_data:Annotated[OAuth2PasswordRequestForm,Depends()],db:db_dependency):
    user = authenticate_user(form_data.username,form_data.password,db)
    if not user :
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate User")
    token = create_access_token(user)
    return{'access_token':token,'token_type':'bearer'}


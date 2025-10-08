from fastapi import  APIRouter,HTTPException,Depends,status
from typing import List
from database.db import db_dependency
from schemas.user_schema.createUserSchema import createUser
from schemas.user_schema.updateUserSchema import UserUpdate
from schemas.user_schema.getUsersListSchema import getUserUsersListSchema
from services.user_services import get_users_service,add_user_service,update_user_service,delete_user_service,hardDelete_user_service,get_user_by_id_service
from utils.auth import get_current_user
# from utils.token import verify_token

router = APIRouter()

@router.get("/get-users",status_code=status.HTTP_200_OK,response_model=List[getUserUsersListSchema])
async def getUsers(db:db_dependency,current_user=Depends(get_current_user)):
   users = get_users_service(db) 
   if users is None:
        raise HTTPException(status_code=404, details='Users not found')
   return users

@router.get("/get-user-by-id/{id}",status_code=status.HTTP_200_OK,response_model=getUserUsersListSchema)
async def getUserById(userId:int,db:db_dependency):
   users = get_user_by_id_service(db,userId) 
   if users is None:
        raise HTTPException(status_code=404, details='Users not found')
   return users

@router.post("/add-user",status_code=status.HTTP_201_CREATED)
async def addUser(UserData: createUser, db:db_dependency,current_user=Depends(get_current_user) ):
    return  add_user_service(UserData, db,current_user) 
    
@router.put("/update-user/{id}",status_code=status.HTTP_200_OK)
async def updateUser(userId:int,updatedUserData: UserUpdate,db:db_dependency,current_user=Depends(get_current_user)):
    return update_user_service(userId,updatedUserData,db,current_user)

@router.put("/delete-user/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def deleteUser(userId:int,db:db_dependency,current_user=Depends(get_current_user)):
    return delete_user_service(userId,db,current_user)

@router.delete("/hard-delete-user/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def hardDelete(userId:int, db:db_dependency):
    return hardDelete_user_service(userId,db)
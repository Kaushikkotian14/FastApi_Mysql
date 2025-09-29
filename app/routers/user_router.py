from fastapi import  APIRouter,HTTPException,Depends,status
from database.db import db_dependency
from schemas.user_schema.createUserSchema import createUser
from schemas.user_schema.updateUserSchema import UserUpdate
from schemas.user_schema.deleteUserSchema import deleteUser
from services.user_services import get_users_service,add_user_service,update_user_service,delete_user_service,hardDelete_user_service

router = APIRouter()

@router.get("/get-users",status_code=status.HTTP_200_OK)
async def getUsers(db:db_dependency):
   users = get_users_service(db)
   if users is None:
        raise HTTPException(status_code=404, details='Users not found')
   return users

@router.post("/add-user",status_code=status.HTTP_201_CREATED)
async def addUser(UserData: createUser, db:db_dependency ):
    return add_user_service(UserData, db) 
    
@router.put("/update-user/{id}",status_code=status.HTTP_200_OK)
async def updateUser(id:int,updatedUserData: UserUpdate,db:db_dependency):
    return update_user_service(id,updatedUserData,db)

@router.put("/delete-user/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def deleteUser(id:int,deleteUserData: deleteUser,db:db_dependency):
    return delete_user_service(id,deleteUserData,db)

@router.delete("/hard-delete-user/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def hardDelete(id:int, db:db_dependency):
    return hardDelete_user_service(id,db)
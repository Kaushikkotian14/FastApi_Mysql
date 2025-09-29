from fastapi import  HTTPException,Depends
from models.userModel import userModel
from datetime import datetime
from repositories.user_repository import get_users_repo,add_user_repo,user_data_by_id_repo,update_user_repo,delete_user_repo



def get_users_service(db):
    get_users_repo(db)


def add_user_service(userData,db):
    usersData = userModel(**userData.model_dump())
    add_user_repo(usersData,db)
    return {"msg": "user created"}

def update_user_service(userId,updatedUserData,db):
    userData=user_data_by_id_repo(userId,db)
    print("hii",userData)
    if userData is None:
        raise HTTPException(status_code=404, details='User not found')
    userData.firstname= updatedUserData.firstname
    userData.lastname= updatedUserData.lastname
    userData.phoneNumber=updatedUserData.phoneNumber
    userData.age=updatedUserData.age
    userData.is_active=updatedUserData.is_active
    userData.changed_by=updatedUserData.changed_by
    update_user_repo(userData,db)
    return {"msg": "user is updated"}

def delete_user_service(userId,deleteUserData,db):
    userData=user_data_by_id_repo(userId,db)
    if userData is None:
        raise HTTPException(status_code=404, details='User not found')
    userData.is_active=deleteUserData.is_active
    userData.deleted_by=deleteUserData.deleted_by
    userData.deleted_at=datetime.now()
    delete_user_repo(userData,db)
    return {"msg": "user deleted"}

def hardDelete_user_service(userId,db):
    userData=user_data_by_id_repo(userId,db)
    if userData is None:
        raise HTTPException(status_code=404, details='User not found')
    db.delete(userData)
    db.commit()
    return {"msg": "user deleted permanently"}

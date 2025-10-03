from fastapi import  HTTPException
from repositories.user_repository import get_users_repo,add_user_repo,user_data_by_id_repo,update_user_repo,delete_user_repo,hardDelete_user_repo

def get_users_service(db):
    return get_users_repo(db)   

def add_user_service(userData,db,current_user):
    add_user_repo(userData,db,current_user)
    return {"msg": "user created"}

def update_user_service(userId,updatedUserData,db,current_user):
    update_user_repo(userId,updatedUserData,db,current_user) 
    return {"msg": "user is updated"}

def delete_user_service(userId,db,current_user):
    delete_user_repo(userId,db,current_user)
    return {"msg": "user deleted"}

def hardDelete_user_service(userId,db):
    hardDelete_user_repo(userId,db)
    return {"msg": "user deleted permanently"}

from models.userModel import userModel
from fastapi import  HTTPException
from datetime import datetime


def user_data_by_id_repo(userId,db):
    userData=db.query(userModel).filter(userModel.userId == userId).first()
    return userData

def get_users_repo(db):
    usersData=db.query(userModel).filter(userModel.deleted_by == None).all()
    return usersData

def add_user_repo(userData,db,current_user):
    userdata = userModel(**userData.model_dump())
    userdata.created_by = current_user.userId
    db.add(userData)
    db.commit()
    db.refresh(userData)

def update_user_repo(userId,updatedUserData,db,current_user):
    userData=user_data_by_id_repo(userId,db)
    if userData is None:
        raise HTTPException(status_code=404, details='User not found')
    userData.firstname= updatedUserData.firstname
    userData.lastname= updatedUserData.lastname
    userData.phoneNumber=updatedUserData.phoneNumber
    userData.age=updatedUserData.age
    userData.is_active=updatedUserData.is_active
    userData.changed_by=current_user.userId
    db.commit()
    db.refresh(userData)
    
def delete_user_repo(userId,db,current_user):
    userData=user_data_by_id_repo(userId,db)
    if userData is None:
        raise HTTPException(status_code=404, details='User not found')
    userData.is_active=False
    userData.deleted_by=current_user.userId
    userData.deleted_at=datetime.now()
    db.commit()
    db.refresh(userData)

def hardDelete_user_repo(userId,db):
    userData=user_data_by_id_repo(userId,db)
    if userData is None:
        raise HTTPException(status_code=404, details='User not found')
    db.delete(userData)
    db.commit()
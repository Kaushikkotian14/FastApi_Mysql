from repositories.user_repository import get_users_repo,add_user_repo,update_user_repo,delete_user_repo,hardDelete_user_repo,user_data_by_id_repo
from schemas.user_schema.getUsersListSchema import getUserUsersListSchema
from fastapi import HTTPException

def get_users_service(db):
    users= get_users_repo(db)
    # usersData=[]
    # for user in users:
    #     userData=getUserUsersListSchema(
    #         firstName= user.firstname, 
    #         lastName=user.lastname, 
    #         phoneNumber=user.phoneNumber,
    #         age=user.age 
    #     )
    #     usersData.append(userData)
    return users


def get_user_by_id_service(db,userId):
    return user_data_by_id_repo(db,userId)   

def add_user_service(userData,db,current_user):
    if(userData.age>18):
     add_user_repo(userData,db,current_user)
     return {"msg": "user created"}
    else:
        raise HTTPException(status_code=400, detail='Age should be above 18')

   

def update_user_service(userId,updatedUserData,db,current_user):
    update_user_repo(userId,updatedUserData,db,current_user) 
    return {"msg": "user is updated"}

def delete_user_service(userId,db,current_user):
    delete_user_repo(userId,db,current_user)
    return {"msg": "user deleted"}

def hardDelete_user_service(userId,db):
    hardDelete_user_repo(userId,db)
    return {"msg": "user deleted permanently"}

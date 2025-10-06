from repositories.personalInfo_repo import personalInfo_by_id_repo, get_personalInfos_repo,update_personalInfo_repo,add_personalInfo_repo,delete_personalInfo_repo,hardDelete_personalInfo_repo
from repositories.user_repository import user_data_by_id_repo
from schemas.personalInfo_schema.getPersonalInfoByIdSchema import getPersonalInfoByIdSchema

def get_personalInfos_service(db):
    return get_personalInfos_repo(db)

def get_personalInfo_by_id_service(personalInfoId,db):
     personalInfo = personalInfo_by_id_repo(personalInfoId,db)
     userInfo=user_data_by_id_repo(db,personalInfo.userId)
     userpersonalInfo=getPersonalInfoByIdSchema(
        personalInfoId=personalInfo.personalInfoId,
        firstname=userInfo.firstname,
        lastname=userInfo.lastname,
        professionalTitle= personalInfo.professionalTitle,
        company= personalInfo.company,
        department=personalInfo.department,
        userId=personalInfo.userId
     )
     return userpersonalInfo

def add_personalInfo_service(personalInfo,db,current_user):
    add_personalInfo_repo(personalInfo,db,current_user)
    return {"msg": "user's personalInfo created"}

def update_personalInfo_service(userId,updatedpersonalInfo,db,current_user):
    update_personalInfo_repo(userId,updatedpersonalInfo,db,current_user)
    return {"msg": "user's personalInfo is updated"}

def delete_personalInfo_service(userId,db,current_user):
    delete_personalInfo_repo(userId,db,current_user)
    return {"msg": "user's personalInfo deleted"}

def hardDelete_personalInfo_service(userId,db):
    hardDelete_personalInfo_repo(userId,db)
    return {"msg": "user's personalInfo deleted permanently"}

from fastapi import  HTTPException
from models.personalInfoModel import personalInfoModel
from datetime import datetime
from repositories.personalInfo_repo import personalInfo_by_id_repo, get_personalInfos_repo,update_personalInfo_repo,add_personalInfo_repo,delete_personalInfo_repo

def get_personalInfos_service(db):
    get_personalInfos_repo(db)

def add_personalInfo_service(personalInfo,db):
    personalInfos = personalInfoModel(**personalInfo.model_dump())
    add_personalInfo_repo(personalInfos,db)
    return {"msg": "user's personalInfo created"}

def update_personalInfo_service(userId,updatedpersonalInfo,db):
    personalInfo=personalInfo_by_id_repo(userId,db)
    if personalInfo is None:
        raise HTTPException(status_code=404, details='User not found')
    personalInfo.professionalTitle= updatedpersonalInfo.professionalTitle
    personalInfo.company= updatedpersonalInfo.company
    personalInfo.department=updatedpersonalInfo.department
    personalInfo.userId=updatedpersonalInfo.userId
    personalInfo.is_active=updatedpersonalInfo.is_active
    personalInfo.changed_by=updatedpersonalInfo.changed_by
    update_personalInfo_repo(personalInfo,db)
    return {"msg": "user's personalInfo is updated"}

def delete_personalInfo_service(userId,deletepersonalInfo,db):
    personalInfo=personalInfo_by_id_repo(userId,db)
    if personalInfo is None:
        raise HTTPException(status_code=404, details='User not found')
    personalInfo.is_active=deletepersonalInfo.is_active
    personalInfo.deleted_by=deletepersonalInfo.deleted_by
    personalInfo.deleted_at=datetime.now()
    delete_personalInfo_repo(personalInfo,db)
    return {"msg": "user's personalInfo deleted"}

def hardDelete_personalInfo_service(userId,db):
    personalInfo=personalInfo_by_id_repo(userId,db)
    if personalInfo is None:
        raise HTTPException(status_code=404, details='User not found')
    db.delete(personalInfo)
    db.commit()
    return {"msg": "user's personalInfo deleted permanently"}

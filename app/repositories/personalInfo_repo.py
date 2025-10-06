from models.personalInfoModel import personalInfoModel
from fastapi import  HTTPException
from datetime import datetime


def personalInfo_by_id_repo(personalInfoId,db):
    personalInfo=db.query(personalInfoModel).filter(personalInfoModel.personalInfoId == personalInfoId).first()
    return personalInfo

def get_personalInfos_repo(db):
    personalInfo=db.query(personalInfoModel).filter(personalInfoModel.deleted_by == None).all()
    return personalInfo

def personalInfo_by_id_repo(personalInfoId,db):
    personalInfo=db.query(personalInfoModel).filter(personalInfoModel.personalInfoId == personalInfoId).first()
    return personalInfo


def add_personalInfo_repo(personalInfo,db,current_user):
    personal_Info = personalInfoModel(**personalInfo.model_dump())
    personal_Info.created_by=current_user.userId
    db.add(personal_Info)
    db.commit()
    db.refresh(personal_Info)

def update_personalInfo_repo(userId,updatedpersonalInfo,db,current_user):
    personalInfo=personalInfo_by_id_repo(userId,db)
    if personalInfo is None:
        raise HTTPException(status_code=404, detail='PersonalInfo not found')
    personalInfo.professionalTitle= updatedpersonalInfo.professionalTitle
    personalInfo.company= updatedpersonalInfo.company
    personalInfo.department=updatedpersonalInfo.department
    personalInfo.userId=updatedpersonalInfo.userId
    personalInfo.is_active=updatedpersonalInfo.is_active
    personalInfo.changed_by=current_user.userId
    db.commit()
    db.refresh(personalInfo)
    
def delete_personalInfo_repo(userId,db,current_user):
    personalInfo=personalInfo_by_id_repo(userId,db)
    if personalInfo is None:
        raise HTTPException(status_code=404, detail='PersonalInfo not found')
    personalInfo.is_active=False
    personalInfo.deleted_by=current_user.userId
    personalInfo.deleted_at=datetime.now()
    db.commit()
    db.refresh(personalInfo)

def hardDelete_personalInfo_repo(userId,db):
    personalInfo=personalInfo_by_id_repo(userId,db)
    if personalInfo is None:
        raise HTTPException(status_code=404, detail='PersonalInfo not found')
    db.delete(personalInfo)
    db.commit()
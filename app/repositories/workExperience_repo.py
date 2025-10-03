from models.workExperienceModel import workExperienceModel
from fastapi import  HTTPException
from datetime import datetime


def workExperience_by_id_repo(workExperienceId,db):
    workExperience=db.query(workExperienceModel).filter(workExperienceModel.workExperienceId == workExperienceId).first()
    return workExperience

def get_workExperiences_repo(db):
    workExperience=db.query(workExperienceModel).filter(workExperienceModel.deleted_by == None).all()
    return workExperience

def add_workExperience_repo(workExperience,db,current_user):
    work_Experience = workExperienceModel(**workExperience.model_dump())
    work_Experience.created_by= current_user.userId
    db.add(work_Experience)
    db.commit()
    db.refresh(work_Experience)

def update_workExperience_repo(userId,updatedworkExperience,db,current_user):
    workExperience=workExperience_by_id_repo(userId,db)
    if workExperience is None:
        raise HTTPException(status_code=404, detail='Work Experience not found')
    workExperience.currentEmployer= updatedworkExperience.currentEmployer
    workExperience.totalYears= updatedworkExperience.totalYears
    workExperience.personalInfoIderId=updatedworkExperience.personalInfoIderId
    workExperience.is_active=updatedworkExperience.is_active
    workExperience.changed_by=current_user.userId
    db.commit()
    db.refresh(workExperience)
    
def delete_workExperience_repo(userId,db,current_user):
    workExperience=workExperience_by_id_repo(userId,db)
    if workExperience is None:
        raise HTTPException(status_code=404, detail='Work Experience not found')
    workExperience.is_active=False
    workExperience.deleted_by=current_user.userId
    workExperience.deleted_at=datetime.now()
    db.commit()
    db.refresh(workExperience)

def hardDelete_workExperience_repo(userId,db):
    workExperience=workExperience_by_id_repo(userId,db)
    if workExperience is None:
        raise HTTPException(status_code=404, detail='Work Experience not found')
    db.delete(workExperience)
    db.commit()
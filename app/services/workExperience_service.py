from fastapi import  HTTPException
from models.workExperienceModel import workExperienceModel
from datetime import datetime
from repositories.workExperience_repo import workExperience_by_id_repo, get_workExperiences_repo,update_workExperience_repo,add_workExperience_repo,delete_workExperience_repo

def get_workExperiences_service(db):
    return get_workExperiences_repo(db)

def add_workExperience_service(workExperience,db):
    workExperiences = workExperienceModel(**workExperience.model_dump())
    add_workExperience_repo(workExperiences,db)
    return {"msg": "user's workExperience created"}

def update_workExperience_service(userId,updatedworkExperience,db):
    workExperience=workExperience_by_id_repo(userId,db)
    if workExperience is None:
        raise HTTPException(status_code=404, details='User not found')
    workExperience.currentEmployer= updatedworkExperience.currentEmployer
    workExperience.totalYears= updatedworkExperience.totalYears
    workExperience.personalInfoIderId=updatedworkExperience.personalInfoIderId
    workExperience.is_active=updatedworkExperience.is_active
    workExperience.changed_by=updatedworkExperience.changed_by
    update_workExperience_repo(workExperience,db)
    return {"msg": "user's workExperience is updated"}

def delete_workExperience_service(userId,deleteworkExperience,db):
    workExperience=workExperience_by_id_repo(userId,db)
    if workExperience is None:
        raise HTTPException(status_code=404, details='User not found')
    workExperience.is_active=deleteworkExperience.is_active
    workExperience.deleted_by=deleteworkExperience.deleted_by
    workExperience.deleted_at=datetime.now()
    delete_workExperience_repo(workExperience,db)
    return {"msg": "user's workExperience deleted"}

def hardDelete_workExperience_service(userId,db):
    workExperience=workExperience_by_id_repo(userId,db)
    if workExperience is None:
        raise HTTPException(status_code=404, details='User not found')
    db.delete(workExperience)
    db.commit()
    return {"msg": "user's workExperience deleted permanently"}

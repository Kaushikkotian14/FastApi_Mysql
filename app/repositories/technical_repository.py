from models.technicalModel import technicalModel
from fastapi import  HTTPException
from datetime import datetime


def technical_by_id_repo(technicalId,db):
    technical=db.query(technicalModel).filter(technicalModel.technicalId == technicalId,technicalModel.deleted_by == None).first()
    if technical is None:
        raise HTTPException(status_code=404, detail='Technical Skill not found')
    return technical

def get_technicals_repo(db):
    technical=db.query(technicalModel).filter(technicalModel.deleted_by == None).all()
    if technical is None:
        raise HTTPException(status_code=404, detail='Technical Skill not found')
    return technical

def add_technical_repo(technical,db,current_user):
    newTechnical = technicalModel(**technical.model_dump())
    newTechnical.created_by= current_user.userId
    db.add(newTechnical)
    db.commit()
    db.refresh(newTechnical)

def update_technical_repo(userId,updatedtechnical,db,current_user):
    technical=technical_by_id_repo(userId,db)
    if technical is None:
        raise HTTPException(status_code=404, detail='Technical Skill not found')
    technical.currentEmployer= updatedtechnical.currentEmployer
    technical.totalYears= updatedtechnical.totalYears
    technical.personalInfoIderId=updatedtechnical.personalInfoIderId
    technical.is_active=updatedtechnical.is_active
    technical.changed_by=current_user.userId
    db.commit()
    db.refresh(technical)
    
def delete_technical_repo(userId,db,current_user):
    technical=technical_by_id_repo(userId,db)
    if technical is None:
        raise HTTPException(status_code=404, detail='Technical Skill not found')
    technical.is_active=False
    technical.deleted_by=current_user.userId
    technical.deleted_at=datetime.now()
    db.commit()
    db.refresh(technical)

def hardDelete_technical_repo(userId,db):
    technical=technical_by_id_repo(userId,db)
    if technical is None:
        raise HTTPException(status_code=404, detail='Technical Skill not found')
    db.delete(technical)
    db.commit()
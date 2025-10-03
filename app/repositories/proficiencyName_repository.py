from models.proficiencyModel import proficiencyModel
from fastapi import  HTTPException
from datetime import datetime


def proficiency_by_id_repo(proficiencyId,db):
    proficiency=db.query(proficiencyModel).filter(proficiencyModel.proficiencyId == proficiencyId).first()
    return proficiency

def get_proficiencys_repo(db):
    proficiency=db.query(proficiencyModel).filter(proficiencyModel.deleted_by == None).all()
    return proficiency

def add_proficiency_repo(proficiency,db,current_user):
    work_Experience = proficiencyModel(**proficiency.model_dump())
    work_Experience.created_by= current_user.userId
    db.add(work_Experience)
    db.commit()
    db.refresh(work_Experience)

def update_proficiency_repo(userId,updatedproficiency,db,current_user):
    proficiency=proficiency_by_id_repo(userId,db)
    if proficiency is None:
        raise HTTPException(status_code=404, detail='Proficiency not found')
    proficiency.name= updatedproficiency.name
    proficiency.proficiency_rating= updatedproficiency.proficiency_rating
    proficiency.is_active=updatedproficiency.is_active
    proficiency.changed_by=current_user.userId
    db.commit()
    db.refresh(proficiency)
    
def delete_proficiency_repo(userId,db,current_user):
    proficiency=proficiency_by_id_repo(userId,db)
    if proficiency is None:
        raise HTTPException(status_code=404, detail='Proficiency not found')
    proficiency.is_active=False
    proficiency.deleted_by=current_user.userId
    proficiency.deleted_at=datetime.now()
    db.commit()
    db.refresh(proficiency)

def hardDelete_proficiency_repo(userId,db):
    proficiency=proficiency_by_id_repo(userId,db)
    if proficiency is None:
        raise HTTPException(status_code=404, detail='Proficiency not found')
    db.delete(proficiency)
    db.commit()
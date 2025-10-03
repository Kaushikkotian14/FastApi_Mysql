from models.proficiencyMappingModel import proficiencymappingModel
from fastapi import  HTTPException
from datetime import datetime


def proficiencyMapping_by_id_repo(proficiencyMappingId,db):
    proficiencyMapping=db.query(proficiencymappingModel).filter(proficiencymappingModel.proficiencyMappingId == proficiencyMappingId).first()
    return proficiencyMapping

def get_proficiencyMappings_repo(db):
    proficiencyMapping=db.query(proficiencymappingModel).filter(proficiencymappingModel.deleted_by == None).all()
    return proficiencyMapping

def add_proficiencyMapping_repo(proficiencyMapping,db,current_user):
    newproficiencymapping = proficiencymappingModel(**proficiencyMapping.model_dump())
    newproficiencymapping.created_by= current_user.userId
    db.add(newproficiencymapping)
    db.commit()
    db.refresh(newproficiencymapping)

def update_proficiencyMapping_repo(userId,updatedproficiencyMapping,db,current_user):
    proficiencyMapping=proficiencyMapping_by_id_repo(userId,db)
    if proficiencyMapping is None:
        raise HTTPException(status_code=404, detail='Proficiency Mapping not found')
    proficiencyMapping.currentEmployer= updatedproficiencyMapping.currentEmployer
    proficiencyMapping.totalYears= updatedproficiencyMapping.totalYears
    proficiencyMapping.personalInfoIderId=updatedproficiencyMapping.personalInfoIderId
    proficiencyMapping.is_active=updatedproficiencyMapping.is_active
    proficiencyMapping.changed_by=current_user.userId
    db.commit()
    db.refresh(proficiencyMapping)
    
def delete_proficiencyMapping_repo(userId,db,current_user):
    proficiencyMapping=proficiencyMapping_by_id_repo(userId,db)
    if proficiencyMapping is None:
        raise HTTPException(status_code=404, detail='Proficiency Mapping not found')
    proficiencyMapping.is_active=False
    proficiencyMapping.deleted_by=current_user.userId
    proficiencyMapping.deleted_at=datetime.now()
    db.commit()
    db.refresh(proficiencyMapping)

def hardDelete_proficiencyMapping_repo(userId,db):
    proficiencyMapping=proficiencyMapping_by_id_repo(userId,db)
    if proficiencyMapping is None:
        raise HTTPException(status_code=404, detail='Proficiency Mapping not found')
    db.delete(proficiencyMapping)
    db.commit()
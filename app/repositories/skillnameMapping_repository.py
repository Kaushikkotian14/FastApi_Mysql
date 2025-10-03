from models.skillnameMappingModel import skillnamemappingModel
from fastapi import  HTTPException
from datetime import datetime


def skillnameMapping_by_id_repo(skillnameMappingId,db):
    skillnameMapping=db.query(skillnamemappingModel).filter(skillnamemappingModel.skillnamemappingId == skillnameMappingId).first()
    return skillnameMapping

def get_skillnameMappings_repo(db):
    skillnameMapping=db.query(skillnamemappingModel).filter(skillnamemappingModel.deleted_by == None).all()
    return skillnameMapping

def add_skillnameMapping_repo(skillnameMapping,db,current_user):
    newskillnameMapping = skillnamemappingModel(**skillnameMapping.model_dump())
    newskillnameMapping.created_by= current_user.userId
    db.add(newskillnameMapping)
    db.commit()
    db.refresh(newskillnameMapping)

def update_skillnameMapping_repo(userId,updatedskillnameMapping,db,current_user):
    skillnameMapping=skillnameMapping_by_id_repo(userId,db)
    if skillnameMapping is None:
        raise HTTPException(status_code=404, detail='Skillname Mapping not found')
    skillnameMapping.technicalId= updatedskillnameMapping.technicalId
    skillnameMapping.skillnameId= updatedskillnameMapping.skillnameId
    skillnameMapping.is_active=updatedskillnameMapping.is_active
    skillnameMapping.changed_by=current_user.userId
    db.commit()
    db.refresh(skillnameMapping)
    
def delete_skillnameMapping_repo(userId,db,current_user):
    skillnameMapping=skillnameMapping_by_id_repo(userId,db)
    if skillnameMapping is None:
        raise HTTPException(status_code=404, detail='Skillname Mapping not found')
    skillnameMapping.is_active=False
    skillnameMapping.deleted_by=current_user.userId
    skillnameMapping.deleted_at=datetime.now()
    db.commit()
    db.refresh(skillnameMapping)

def hardDelete_skillnameMapping_repo(userId,db):
    skillnameMapping=skillnameMapping_by_id_repo(userId,db)
    if skillnameMapping is None:
        raise HTTPException(status_code=404, detail='Skillname Mapping not found')
    db.delete(skillnameMapping)
    db.commit()
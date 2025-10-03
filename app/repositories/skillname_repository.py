from models.skillnameModel import skillnameModel
from fastapi import  HTTPException
from datetime import datetime


def skillname_by_id_repo(skillnameId,db):
    skillname=db.query(skillnameModel).filter(skillnameModel.skillnameId == skillnameId).first()
    return skillname

def get_skillnames_repo(db):
    skillname=db.query(skillnameModel).filter(skillnameModel.deleted_by == None).all()
    return skillname

def add_skillname_repo(skillname,db,current_user):
    newSkillname = skillnameModel(**skillname.model_dump())
    newSkillname.created_by= current_user.userId
    db.add(newSkillname)
    db.commit()
    db.refresh(newSkillname)

def update_skillname_repo(userId,updatedskillname,db,current_user):
    skillname=skillname_by_id_repo(userId,db)
    if skillname is None:
        raise HTTPException(status_code=404, detail='Skillname not found')
    skillname.name= updatedskillname.name
    skillname.is_active=updatedskillname.is_active
    skillname.changed_by=current_user.userId
    db.commit()
    db.refresh(skillname)
    
def delete_skillname_repo(userId,db,current_user):
    skillname=skillname_by_id_repo(userId,db)
    if skillname is None:
        raise HTTPException(status_code=404, detail='Skillname not found')
    skillname.is_active=False
    skillname.deleted_by=current_user.userId
    skillname.deleted_at=datetime.now()
    db.commit()
    db.refresh(skillname)

def hardDelete_skillname_repo(userId,db):
    skillname=skillname_by_id_repo(userId,db)
    if skillname is None:
        raise HTTPException(status_code=404, detail='Skillname not found')
    db.delete(skillname)
    db.commit()
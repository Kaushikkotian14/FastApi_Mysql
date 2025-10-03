from models.softskillModel import softModel
from fastapi import  HTTPException
from datetime import datetime


def softSkill_by_id_repo(softSkillId,db):
    softSkill=db.query(softModel).filter(softModel.softSkillId == softSkillId).first()
    return softSkill

def get_softSkills_repo(db):
    softSkill=db.query(softModel).filter(softModel.deleted_by == None).all()
    return softSkill

def add_softSkill_repo(softSkill,db,current_user):
    soft_Skill = softModel(**softSkill.model_dump())
    soft_Skill.created_by= current_user.userId
    db.add(soft_Skill)
    db.commit()
    db.refresh(soft_Skill)

def update_softSkill_repo(userId,updatedsoftSkill,db,current_user):
    softSkill=softSkill_by_id_repo(userId,db)
    if softSkill is None:
        raise HTTPException(status_code=404, detail='Soft Skill not found')
    softSkill.skillId= updatedsoftSkill.skillId
    softSkill.skill= updatedsoftSkill.skill
    softSkill.skillLevel=updatedsoftSkill.skillLevel 
    softSkill.experience=updatedsoftSkill.experience
    softSkill.is_active=updatedsoftSkill.is_active
    softSkill.changed_by=current_user.userId
    db.commit()
    db.refresh(softSkill)
    
def delete_softSkill_repo(userId,db,current_user):
    softSkill=softSkill_by_id_repo(userId,db)
    if softSkill is None:
        raise HTTPException(status_code=404, detail='Soft Skill not found')
    softSkill.is_active=False
    softSkill.deleted_by=current_user.userId
    softSkill.deleted_at=datetime.now()
    db.commit()
    db.refresh(softSkill)

def hardDelete_softSkill_repo(userId,db):
    softSkill=softSkill_by_id_repo(userId,db)
    if softSkill is None:
        raise HTTPException(status_code=404, detail='Soft Skill not found')
    db.delete(softSkill)
    db.commit()
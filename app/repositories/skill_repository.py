from models.skillModel import skillModel
from fastapi import  HTTPException
from datetime import datetime


def skill_by_id_repo(skillId,db):
    skill=db.query(skillModel).filter(skillModel.skillId == skillId).first()
    return skill

def get_skills_repo(db):
    skills=db.query(skillModel).filter(skillModel.deleted_by == None).all()
    return skills

def add_skill_repo(skill,db,current_user):
    newSkill = skillModel(**skill.model_dump())
    newSkill.created_by= current_user.userId
    db.add(newSkill)
    db.commit()
    db.refresh(newSkill)

def update_skill_repo(userId,updatedskill,db,current_user):
    skill=skill_by_id_repo(userId,db)
    if skill is None:
        raise HTTPException(status_code=404, detail='Skill not found')
    skill.workExperienceId= updatedskill.workExperienceId
    skill.is_active=updatedskill.is_active
    skill.changed_by=current_user.userId
    db.commit()
    db.refresh(skill)
    
def delete_skill_repo(userId,db,current_user):
    skill=skill_by_id_repo(userId,db)
    if skill is None:
        raise HTTPException(status_code=404, detail='Skill not found')
    skill.is_active=False
    skill.deleted_by=current_user.userId
    skill.deleted_at=datetime.now()
    db.commit()
    db.refresh(skill)

def hardDelete_skill_repo(userId,db):
    skill=skill_by_id_repo(userId,db)
    if skill is None:
        raise HTTPException(status_code=404, detail='Skill not found')
    db.delete(skill)
    db.commit()
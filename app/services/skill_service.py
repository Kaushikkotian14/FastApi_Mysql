from repositories.skill_repository import  get_skills_repo,update_skill_repo,add_skill_repo,delete_skill_repo,hardDelete_skill_repo

def get_skills_service(db):
    return get_skills_repo(db)

def add_skill_service(skill,db,current_user):
    add_skill_repo(skill,db,current_user)
    return {"msg": "user's skill created"}

def update_skill_service(userId,updatedskill,db,current_user):
    update_skill_repo(userId,updatedskill,db,current_user)
    return {"msg": "user's skill is updated"}

def delete_skill_service(userId,db,current_user):
    delete_skill_repo(userId,db,current_user)
    return {"msg": "user's skill deleted"}

def hardDelete_skill_service(userId,db):
    hardDelete_skill_repo(userId,db)
    return {"msg": "user's skill deleted permanently"}

from repositories.softskill_repository import  get_softSkills_repo,update_softSkill_repo,add_softSkill_repo,delete_softSkill_repo,hardDelete_softSkill_repo

def get_softSkills_service(db):
    return get_softSkills_repo(db)

def add_softSkill_service(softSkill,db,current_user):
    add_softSkill_repo(softSkill,db,current_user)
    return {"msg": "user's softSkill created"}

def update_softSkill_service(userId,updatedsoftSkill,db,current_user):
    update_softSkill_repo(userId,updatedsoftSkill,db,current_user)
    return {"msg": "user's softSkill is updated"}

def delete_softSkill_service(userId,db,current_user):
    delete_softSkill_repo(userId,db,current_user)
    return {"msg": "user's softSkill deleted"}

def hardDelete_softSkill_service(userId,db):
    hardDelete_softSkill_repo(userId,db)
    return {"msg": "user's softSkill deleted permanently"}

from repositories.skillname_repository import  get_skillnames_repo,update_skillname_repo,add_skillname_repo,delete_skillname_repo,hardDelete_skillname_repo

def get_skillnames_service(db):
    return get_skillnames_repo(db)

def add_skillname_service(skillname,db,current_user):
    add_skillname_repo(skillname,db,current_user)
    return {"msg": "user's skillname created"}

def update_skillname_service(userId,updatedskillname,db,current_user):
    update_skillname_repo(userId,updatedskillname,db,current_user)
    return {"msg": "user's skillname is updated"}

def delete_skillname_service(userId,db,current_user):
    delete_skillname_repo(userId,db,current_user)
    return {"msg": "user's skillname deleted"}

def hardDelete_skillname_service(userId,db):
    hardDelete_skillname_repo(userId,db)
    return {"msg": "user's skillname deleted permanently"}

from repositories.skillnameMapping_repository import  get_skillnameMappings_repo,update_skillnameMapping_repo,add_skillnameMapping_repo,delete_skillnameMapping_repo,hardDelete_skillnameMapping_repo

def get_skillnameMappings_service(db):
    return get_skillnameMappings_repo(db)

def add_skillnameMapping_service(skillnameMapping,db,current_user):
    add_skillnameMapping_repo(skillnameMapping,db,current_user)
    return {"msg": "user's skillnameMapping created"}

def update_skillnameMapping_service(userId,updatedskillnameMapping,db,current_user):
    update_skillnameMapping_repo(userId,updatedskillnameMapping,db,current_user)
    return {"msg": "user's skillnameMapping is updated"}

def delete_skillnameMapping_service(userId,db,current_user):
    delete_skillnameMapping_repo(userId,db,current_user)
    return {"msg": "user's skillnameMapping deleted"}

def hardDelete_skillnameMapping_service(userId,db):
    hardDelete_skillnameMapping_repo(userId,db)
    return {"msg": "user's skillnameMapping deleted permanently"}

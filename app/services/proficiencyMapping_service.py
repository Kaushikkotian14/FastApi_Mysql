from repositories.proficiencyNameMapping_repository import  get_proficiencyMappings_repo,update_proficiencyMapping_repo,add_proficiencyMapping_repo,delete_proficiencyMapping_repo,hardDelete_proficiencyMapping_repo

def get_proficiencyMappings_service(db):
    return get_proficiencyMappings_repo(db)

def add_proficiencyMapping_service(proficiencyMapping,db,current_user):
    add_proficiencyMapping_repo(proficiencyMapping,db,current_user)
    return {"msg": "user's proficiencyMapping created"}

def update_proficiencyMapping_service(userId,updatedproficiencyMapping,db,current_user):
    update_proficiencyMapping_repo(userId,updatedproficiencyMapping,db,current_user)
    return {"msg": "user's proficiencyMapping is updated"}

def delete_proficiencyMapping_service(userId,db,current_user):
    delete_proficiencyMapping_repo(userId,db,current_user)
    return {"msg": "user's proficiencyMapping deleted"}

def hardDelete_proficiencyMapping_service(userId,db):
    hardDelete_proficiencyMapping_repo(userId,db)
    return {"msg": "user's proficiencyMapping deleted permanently"}

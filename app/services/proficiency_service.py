from repositories.proficiencyName_repository import  get_proficiencys_repo,update_proficiency_repo,add_proficiency_repo,delete_proficiency_repo,hardDelete_proficiency_repo

def get_proficiencys_service(db):
    return get_proficiencys_repo(db)

def add_proficiency_service(proficiency,db,current_user):
    add_proficiency_repo(proficiency,db,current_user)
    return {"msg": "user's proficiency created"}

def update_proficiency_service(userId,updatedproficiency,db,current_user):
    update_proficiency_repo(userId,updatedproficiency,db,current_user)
    return {"msg": "user's proficiency is updated"}

def delete_proficiency_service(userId,db,current_user):
    delete_proficiency_repo(userId,db,current_user)
    return {"msg": "user's proficiency deleted"}

def hardDelete_proficiency_service(userId,db):
    hardDelete_proficiency_repo(userId,db)
    return {"msg": "user's proficiency deleted permanently"}

from repositories.workExperience_repo import  get_workExperiences_repo,update_workExperience_repo,add_workExperience_repo,delete_workExperience_repo,hardDelete_workExperience_repo

def get_workExperiences_service(db):
    return get_workExperiences_repo(db)

def add_workExperience_service(workExperience,db,current_user):
    add_workExperience_repo(workExperience,db,current_user)
    return {"msg": "user's workExperience created"}

def update_workExperience_service(userId,updatedworkExperience,db,current_user):
    update_workExperience_repo(userId,updatedworkExperience,db,current_user)
    return {"msg": "user's workExperience is updated"}

def delete_workExperience_service(userId,db,current_user):
    delete_workExperience_repo(userId,db,current_user)
    return {"msg": "user's workExperience deleted"}

def hardDelete_workExperience_service(userId,db):
    hardDelete_workExperience_repo(userId,db)
    return {"msg": "user's workExperience deleted permanently"}

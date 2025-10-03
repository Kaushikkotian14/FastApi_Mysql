from repositories.personalInfo_repo import personalInfo_by_id_repo, get_personalInfos_repo,update_personalInfo_repo,add_personalInfo_repo,delete_personalInfo_repo,hardDelete_personalInfo_repo

def get_personalInfos_service(db):
    return get_personalInfos_repo(db)

def add_personalInfo_service(personalInfo,db,current_user):
    add_personalInfo_repo(personalInfo,db,current_user)
    return {"msg": "user's personalInfo created"}

def update_personalInfo_service(userId,updatedpersonalInfo,db,current_user):
    update_personalInfo_repo(userId,updatedpersonalInfo,db,current_user)
    return {"msg": "user's personalInfo is updated"}

def delete_personalInfo_service(userId,db,current_user):
    delete_personalInfo_repo(userId,db,current_user)
    return {"msg": "user's personalInfo deleted"}

def hardDelete_personalInfo_service(userId,db):
    hardDelete_personalInfo_repo(userId,db)
    return {"msg": "user's personalInfo deleted permanently"}

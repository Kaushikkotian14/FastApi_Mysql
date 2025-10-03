from repositories.technical_repository import  get_technicals_repo,update_technical_repo,add_technical_repo,delete_technical_repo,hardDelete_technical_repo

def get_technicals_service(db):
    return get_technicals_repo(db)

def add_technical_service(technical,db,current_user):
    add_technical_repo(technical,db,current_user)
    return {"msg": "user's Technical Skill created"}

def update_technical_service(userId,updatedtechnical,db,current_user):
    update_technical_repo(userId,updatedtechnical,db,current_user)
    return {"msg": "user's Technical Skill is updated"}

def delete_technical_service(userId,db,current_user):
    delete_technical_repo(userId,db,current_user)
    return {"msg": "user's Technical Skill deleted"}

def hardDelete_technical_service(userId,db):
    hardDelete_technical_repo(userId,db)
    return {"msg": "user's Technical Skill deleted permanently"}

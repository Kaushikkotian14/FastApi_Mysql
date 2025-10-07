from repositories.workExperience_repo import  get_workExperiences_repo,update_workExperience_repo,add_workExperience_repo,delete_workExperience_repo,hardDelete_workExperience_repo,workExperience_by_id_repo
from repositories.personalInfo_repo import personalInfo_by_id_repo
from repositories.user_repository import user_data_by_id_repo
from schemas.workExperience_schema.getworkExperienceByIdSchema import getworkExperienceByIdSchema
from schemas.workExperience_schema.getworkExperienceListSchema import getworkExperienceListSchema

def get_workExperiences_service(db):
     workExperiences=get_workExperiences_repo(db)
     workExperienceList=[]
     for workExperience in workExperiences:
        userWorkExperience = workExperience_by_id_repo(workExperience.workExperienceId,db)
        userpersonalInfo = personalInfo_by_id_repo(userWorkExperience.personalInfoId,db)
        userData = user_data_by_id_repo(db,userpersonalInfo.userId)
        userWorkExperienceData=getworkExperienceListSchema(
            firstname=userData.firstname,
            lastname=userData.lastname,
            currentEmployer=userWorkExperience.currentEmployer, 
            totalYears=userWorkExperience.totalYears,
        )
        workExperienceList.append(userWorkExperienceData)
     return workExperienceList

def get_workExperience_by_id_service(workexperienceId,db):
    userWorkExperience = workExperience_by_id_repo(workexperienceId,db)
    userpersonalInfo = personalInfo_by_id_repo(userWorkExperience.personalInfoId,db)
    userData = user_data_by_id_repo(db,userpersonalInfo.userId)
    userWorkExperienceData=getworkExperienceByIdSchema(
         workExperienceId=userWorkExperience.workExperienceId,
         userId=userData.userId,
        firstname=userData.firstname,
        lastname=userData.lastname,
        currentEmployer=userWorkExperience.currentEmployer, 
        totalYears=userWorkExperience.totalYears,
        personalInfoId=userWorkExperience.personalInfoId
    )
    return userWorkExperienceData

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

from fastapi import  APIRouter,HTTPException,Depends,status
from database.db import db_dependency
from models.workExperienceModel import workExperienceModel
from schemas.workExperience_schema.createWorkExperienceSchema import createWorkExperience
from schemas.workExperience_schema.updateWorkExperienceSchema import updateWorkExperience
from schemas.workExperience_schema.deleteWorkExperienceSchema import  deleteWorkExperience
from services.workExperience_service import get_workExperiences_service,update_workExperience_service,add_workExperience_service,delete_workExperience_service,hardDelete_workExperience_service

router = APIRouter()

@router.get("/get-workexperience",status_code=status.HTTP_200_OK)
async def getWorkExperiences(db:db_dependency):
    workExperiences=get_workExperiences_service(db)
    if workExperiences is None:
        raise HTTPException(status_code=404, details='Data not found')
    return workExperiences


@router.post("/add-workExperience",status_code=status.HTTP_201_CREATED)
async def addworkExperience(workExperience: createWorkExperience, db:db_dependency ):
    return add_workExperience_service(workExperience, db) 
    
@router.put("/update-workExperience/{id}",status_code=status.HTTP_200_OK)
async def updateworkExperience(id:int,updatedworkExperience: updateWorkExperience,db:db_dependency):
    return update_workExperience_service(id,updatedworkExperience,db)

@router.put("/delete-workExperience/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def deleteworkExperience(id:int,deleteworkExperience: deleteWorkExperience,db:db_dependency):
    return delete_workExperience_service(id,deleteworkExperience,db)

@router.delete("/hard-delete-workExperience/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def hardDeleteworkExperience(id:int, db:db_dependency):
    return hardDelete_workExperience_service(id,db)
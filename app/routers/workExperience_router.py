from fastapi import  APIRouter,HTTPException,Depends,status
from database.db import db_dependency
from schemas.workExperience_schema.createWorkExperienceSchema import createWorkExperience
from schemas.workExperience_schema.updateWorkExperienceSchema import updateWorkExperience
from services.workExperience_service import get_workExperiences_service,update_workExperience_service,add_workExperience_service,delete_workExperience_service,hardDelete_workExperience_service
from utils.auth import get_current_user


router = APIRouter()

@router.get("/get-workexperience",status_code=status.HTTP_200_OK)
async def getWorkExperiences(db:db_dependency):
    workExperiences=get_workExperiences_service(db)
    if workExperiences is None:
        raise HTTPException(status_code=404, detail='Data not found')
    return workExperiences


@router.post("/add-workExperience",status_code=status.HTTP_201_CREATED)
async def addworkExperience(workExperience: createWorkExperience, db:db_dependency,current_user=Depends(get_current_user) ):
    return add_workExperience_service(workExperience, db,current_user) 
    
@router.put("/update-workExperience/{id}",status_code=status.HTTP_200_OK)
async def updateworkExperience(id:int,updatedworkExperience: updateWorkExperience,db:db_dependency,current_user=Depends(get_current_user)):
    return update_workExperience_service(id,updatedworkExperience,db,current_user)

@router.put("/delete-workExperience/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def deleteworkExperience(id:int,db:db_dependency,current_user=Depends(get_current_user)):
    return delete_workExperience_service(id,db,current_user)

@router.delete("/hard-delete-workExperience/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def hardDeleteworkExperience(id:int, db:db_dependency):
    return hardDelete_workExperience_service(id,db)
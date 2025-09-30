from fastapi import  APIRouter,HTTPException,Depends,status
from database.db import db_dependency
from models.personalInfoModel import personalInfoModel
from schemas.personalInfo_schema.createPersonalInfoSchema import createPersonalInfo
from schemas.personalInfo_schema.updatePersonalInfoSchema import updatePersonalInfo
from schemas.personalInfo_schema.deletePersonalInfoSchema import  deletePersonalInfo
from services.personalInfo_service import get_personalInfos_service,update_personalInfo_service,add_personalInfo_service,delete_personalInfo_service,hardDelete_personalInfo_service

router = APIRouter()


@router.get("/get-personalInfo",status_code=status.HTTP_200_OK)
async def getPersonalInfos(db:db_dependency):
    data=db.query(personalInfoModel).all()
    if data is None:
        raise HTTPException(status_code=404, details='Data not found')
    return  data


@router.post("/add-personalInfo",status_code=status.HTTP_201_CREATED)
async def addpersonalInfo(personalInfo: createPersonalInfo, db:db_dependency ):
    return  add_personalInfo_service(personalInfo, db) 
    
@router.put("/update-personalInfo/{id}",status_code=status.HTTP_200_OK)
async def updatePersonalInfo(id:int,updatedPersonalInfo: updatePersonalInfo,db:db_dependency):
    return  update_personalInfo_service(id,updatedPersonalInfo,db)

@router.put("/delete-personalInfo/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def deletePersonalInfo(id:int,deletePersonalInfo: deletePersonalInfo,db:db_dependency):
    return  delete_personalInfo_service(id,deletePersonalInfo,db)

@router.delete("/hard-delete-personalInfo/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def hardDeletePersonalInfo(id:int, db:db_dependency):
    return  hardDelete_personalInfo_service(id,db)
from fastapi import  APIRouter,HTTPException,Depends,status
from typing import List
from database.db import db_dependency
from schemas.personalInfo_schema.createPersonalInfoSchema import createPersonalInfo
from schemas.personalInfo_schema.updatePersonalInfoSchema import updatePersonalInfo
from schemas.personalInfo_schema.getPersonalInfoListSchema import getPersonalInfoListSchema
from schemas.personalInfo_schema.getPersonalInfoByIdSchema import getPersonalInfoByIdSchema
from services.personalInfo_service import get_personalInfos_service,update_personalInfo_service,add_personalInfo_service,delete_personalInfo_service,hardDelete_personalInfo_service,get_personalInfo_by_id_service
from utils.auth import get_current_user


router = APIRouter()

@router.get("/get-personalInfo",status_code=status.HTTP_200_OK,response_model=List[getPersonalInfoListSchema])
async def getPersonalInfos(db:db_dependency):
    getPersonalInfos=get_personalInfos_service(db)
    if getPersonalInfos is None:
        raise HTTPException(status_code=404, detail='Data not found')
    return  getPersonalInfos

@router.get("/get-personalInfo-by-id/{id}",status_code=status.HTTP_200_OK,response_model=getPersonalInfoByIdSchema)
async def getPersonalInfoById(personalInfoId:int,db:db_dependency):
    getPersonalInfo=get_personalInfo_by_id_service(personalInfoId,db)
    if getPersonalInfo is None:
        raise HTTPException(status_code=404, detail='Data not found')
    return  getPersonalInfo


@router.post("/add-personalInfo",status_code=status.HTTP_201_CREATED)
async def addpersonalInfo(personalInfo: createPersonalInfo, db:db_dependency,current_user=Depends(get_current_user) ):
    return  add_personalInfo_service(personalInfo, db,current_user) 
    
@router.put("/update-personalInfo/{id}",status_code=status.HTTP_200_OK)
async def updatePersonalInfo(personalInfoId:int,updatedPersonalInfo: updatePersonalInfo,db:db_dependency,current_user=Depends(get_current_user)):
    return  update_personalInfo_service(id,updatedPersonalInfo,db,current_user)

@router.put("/delete-personalInfo/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def deletePersonalInfo(id:int,db:db_dependency,current_user=Depends(get_current_user)):
    return  delete_personalInfo_service(id,db,current_user)

@router.delete("/hard-delete-personalInfo/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def hardDeletePersonalInfo(id:int, db:db_dependency):
    return  hardDelete_personalInfo_service(id,db)
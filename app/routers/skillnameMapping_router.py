from fastapi import  APIRouter,HTTPException,Depends,status
from database.db import db_dependency
from schemas.skillnameMapping_schema.createskillnameMappingSchema import createSkillnameMappingSchema
from schemas.skillnameMapping_schema.updateSkillnameMappingSchema import updateSkillnameMappingSchema
from services.skillnameMapping_service import get_skillnameMappings_service,update_skillnameMapping_service,add_skillnameMapping_service,delete_skillnameMapping_service,hardDelete_skillnameMapping_service
from utils.auth import get_current_user


router = APIRouter()

@router.get("/get-skillnameMapping",status_code=status.HTTP_200_OK)
async def getskillnameMappings(db:db_dependency):
    skillnameMappings=get_skillnameMappings_service(db)
    if skillnameMappings is None:
        raise HTTPException(status_code=404, detail='Skillname Mapping not found')
    return skillnameMappings


@router.post("/add-skillnameMapping",status_code=status.HTTP_201_CREATED)
async def addskillnameMapping(skillnameMapping: createSkillnameMappingSchema, db:db_dependency,current_user=Depends(get_current_user) ):
    return add_skillnameMapping_service(skillnameMapping, db,current_user) 
    
@router.put("/update-skillnameMapping/{id}",status_code=status.HTTP_200_OK)
async def updateskillnameMapping(id:int,updatedskillnameMapping: updateSkillnameMappingSchema,db:db_dependency,current_user=Depends(get_current_user)):
    return update_skillnameMapping_service(id,updatedskillnameMapping,db,current_user)

@router.put("/delete-skillnameMapping/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def deleteskillnameMapping(id:int,db:db_dependency,current_user=Depends(get_current_user)):
    return delete_skillnameMapping_service(id,db,current_user)

@router.delete("/hard-delete-skillnameMapping/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def hardDeleteskillnameMapping(id:int, db:db_dependency):
    return hardDelete_skillnameMapping_service(id,db)
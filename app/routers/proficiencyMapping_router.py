from fastapi import  APIRouter,HTTPException,Depends,status
from database.db import db_dependency
from schemas.proficiencyMapping_schema.createproficiencynameMappingSchema import createProficiencynameMappingSchema
from schemas.proficiencyMapping_schema.updateproficiencynameMappingSchema import updateProficiencynameMappingSchema
from services.proficiencyMapping_service import get_proficiencyMappings_service,update_proficiencyMapping_service,add_proficiencyMapping_service,delete_proficiencyMapping_service,hardDelete_proficiencyMapping_service
from utils.auth import get_current_user

router = APIRouter()

@router.get("/get-proficiencyMapping",status_code=status.HTTP_200_OK)
async def getproficiencyMappings(db:db_dependency):
    proficiencyMappings=get_proficiencyMappings_service(db)
    if proficiencyMappings is None:
        raise HTTPException(status_code=404, detail='Proficiency Mapping not found')
    return proficiencyMappings

@router.post("/add-proficiencyMapping",status_code=status.HTTP_201_CREATED)
async def addproficiencyMapping(proficiencyMapping: createProficiencynameMappingSchema, db:db_dependency,current_user=Depends(get_current_user) ):
    return add_proficiencyMapping_service(proficiencyMapping, db,current_user) 
    
@router.put("/update-proficiencyMapping/{id}",status_code=status.HTTP_200_OK)
async def updateproficiencyMapping(id:int,updatedproficiencyMapping: updateProficiencynameMappingSchema,db:db_dependency,current_user=Depends(get_current_user)):
    return update_proficiencyMapping_service(id,updatedproficiencyMapping,db,current_user)

@router.put("/delete-proficiencyMapping/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def deleteproficiencyMapping(id:int,db:db_dependency,current_user=Depends(get_current_user)):
    return delete_proficiencyMapping_service(id,db,current_user)

@router.delete("/hard-delete-proficiencyMapping/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def hardDeleteproficiencyMapping(id:int, db:db_dependency):
    return hardDelete_proficiencyMapping_service(id,db)
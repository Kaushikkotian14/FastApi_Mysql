from fastapi import  APIRouter,HTTPException,Depends,status
from database.db import db_dependency
from schemas.proficiency_schema.creareProficiencynameSchema import createProficiencynameSchema
from schemas.proficiency_schema.updateProficiencynameSchema import updateProficiencynameSchema
from services.proficiency_service import get_proficiencys_service,update_proficiency_service,add_proficiency_service,delete_proficiency_service,hardDelete_proficiency_service
from utils.auth import get_current_user


router = APIRouter()

@router.get("/get-proficiency",status_code=status.HTTP_200_OK)
async def getproficiencys(db:db_dependency):
    proficiencys=get_proficiencys_service(db)
    if proficiencys is None:
        raise HTTPException(status_code=404, detail='Data not found')
    return proficiencys


@router.post("/add-proficiency",status_code=status.HTTP_201_CREATED)
async def addproficiency(proficiency: createProficiencynameSchema, db:db_dependency,current_user=Depends(get_current_user) ):
    return add_proficiency_service(proficiency, db,current_user) 
    
@router.put("/update-proficiency/{id}",status_code=status.HTTP_200_OK)
async def updateproficiency(id:int,updatedproficiency: updateProficiencynameSchema,db:db_dependency,current_user=Depends(get_current_user)):
    return update_proficiency_service(id,updatedproficiency,db,current_user)

@router.put("/delete-proficiency/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def deleteproficiency(id:int,db:db_dependency,current_user=Depends(get_current_user)):
    return delete_proficiency_service(id,db,current_user)

@router.delete("/hard-delete-proficiency/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def hardDeleteproficiency(id:int, db:db_dependency):
    return hardDelete_proficiency_service(id,db)
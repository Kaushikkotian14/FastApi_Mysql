from fastapi import  APIRouter,HTTPException,Depends,status
from database.db import db_dependency
from schemas.softSkill_schema.createSoftSkillSchema import createSoftSkillSchema
from schemas.softSkill_schema.updateSoftSkillSchema import updateSoftSkillSchema
from services.softskill_service import get_softSkills_service,update_softSkill_service,add_softSkill_service,delete_softSkill_service,hardDelete_softSkill_service
from utils.auth import get_current_user


router = APIRouter()

@router.get("/get-softSkill",status_code=status.HTTP_200_OK)
async def getsoftSkills(db:db_dependency):
    softSkills=get_softSkills_service(db)
    if softSkills is None:
        raise HTTPException(status_code=404, detail='Data not found')
    return softSkills


@router.post("/add-softSkill",status_code=status.HTTP_201_CREATED)
async def addsoftSkill(softSkill: createSoftSkillSchema, db:db_dependency,current_user=Depends(get_current_user) ):
    return add_softSkill_service(softSkill, db,current_user) 
    
@router.put("/update-softSkill/{id}",status_code=status.HTTP_200_OK)
async def updatesoftSkill(id:int,updatedsoftSkill: updateSoftSkillSchema,db:db_dependency,current_user=Depends(get_current_user)):
    return update_softSkill_service(id,updatedsoftSkill,db,current_user)

@router.put("/delete-softSkill/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def deletesoftSkill(id:int,db:db_dependency,current_user=Depends(get_current_user)):
    return delete_softSkill_service(id,db,current_user)

@router.delete("/hard-delete-softSkill/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def hardDeletesoftSkill(id:int, db:db_dependency):
    return hardDelete_softSkill_service(id,db)
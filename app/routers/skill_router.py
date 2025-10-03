from fastapi import  APIRouter,HTTPException,Depends,status
from database.db import db_dependency
from schemas.skill_schema.createSkillSchema import createSkillSchema
from schemas.skill_schema.updateSkillSchema import updateSkillSchema
from services.skill_service import get_skills_service,update_skill_service,add_skill_service,delete_skill_service,hardDelete_skill_service
from utils.auth import get_current_user


router = APIRouter()

@router.get("/get-skill",status_code=status.HTTP_200_OK)
async def getskills(db:db_dependency):
    skills=get_skills_service(db)
    if skills is None:
        raise HTTPException(status_code=404, detail='Skills not found')
    return skills


@router.post("/add-skill",status_code=status.HTTP_201_CREATED)
async def addskill(skill: createSkillSchema, db:db_dependency,current_user=Depends(get_current_user) ):
    return add_skill_service(skill, db,current_user) 
    
@router.put("/update-skill/{id}",status_code=status.HTTP_200_OK)
async def updateskill(id:int,updatedskill: updateSkillSchema,db:db_dependency,current_user=Depends(get_current_user)):
    return update_skill_service(id,updatedskill,db,current_user)

@router.put("/delete-skill/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def deleteskill(id:int,db:db_dependency,current_user=Depends(get_current_user)):
    return delete_skill_service(id,db,current_user)

@router.delete("/hard-delete-skill/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def hardDeleteskill(id:int, db:db_dependency):
    return hardDelete_skill_service(id,db)
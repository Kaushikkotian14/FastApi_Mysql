from fastapi import  APIRouter,HTTPException,Depends,status
from database.db import db_dependency
from schemas.skillname_schema.createSkillnameSchema import createSkillnameSchema
from schemas.skillname_schema.updateSkillnameSchema import updateSkillnameSchema
from services.skillname_service import get_skillnames_service,update_skillname_service,add_skillname_service,delete_skillname_service,hardDelete_skillname_service
from utils.auth import get_current_user


router = APIRouter()

@router.get("/get-skillname",status_code=status.HTTP_200_OK)
async def getskillnames(db:db_dependency):
    skillnames=get_skillnames_service(db)
    if skillnames is None:
        raise HTTPException(status_code=404, detail='Data not found')
    return skillnames


@router.post("/add-skillname",status_code=status.HTTP_201_CREATED)
async def addskillname(skillname: createSkillnameSchema, db:db_dependency,current_user=Depends(get_current_user) ):
    return add_skillname_service(skillname, db,current_user) 
    
@router.put("/update-skillname/{id}",status_code=status.HTTP_200_OK)
async def updateskillname(id:int,updatedskillname: updateSkillnameSchema,db:db_dependency,current_user=Depends(get_current_user)):
    return update_skillname_service(id,updatedskillname,db,current_user)

@router.put("/delete-skillname/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def deleteskillname(id:int,db:db_dependency,current_user=Depends(get_current_user)):
    return delete_skillname_service(id,db,current_user)

@router.delete("/hard-delete-skillname/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def hardDeleteskillname(id:int, db:db_dependency):
    return hardDelete_skillname_service(id,db)
from fastapi import  APIRouter,HTTPException,Depends,status
from database.db import db_dependency
from schemas.technical_schema.createTechnicalSchema import createTechnicalSchema
from schemas.technical_schema.updateTechnicalSchema import updateTechnicalSchema
from services.technical_service import get_technicals_service,update_technical_service,add_technical_service,delete_technical_service,hardDelete_technical_service
from utils.auth import get_current_user

router = APIRouter()

@router.get("/get-technical",status_code=status.HTTP_200_OK)
async def gettechnicals(db:db_dependency):
    technicals=get_technicals_service(db)
    if technicals is None:
        raise HTTPException(status_code=404, detail='Technical Skills not found')
    return technicals

@router.post("/add-technical",status_code=status.HTTP_201_CREATED)
async def addtechnical(technical: createTechnicalSchema, db:db_dependency,current_user=Depends(get_current_user) ):
    return add_technical_service(technical, db,current_user) 
    
@router.put("/update-technical/{id}",status_code=status.HTTP_200_OK)
async def updatetechnical(id:int,updatedtechnical: updateTechnicalSchema,db:db_dependency,current_user=Depends(get_current_user)):
    return update_technical_service(id,updatedtechnical,db,current_user)

@router.put("/delete-technical/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def deletetechnical(id:int,db:db_dependency,current_user=Depends(get_current_user)):
    return delete_technical_service(id,db,current_user)

@router.delete("/hard-delete-technical/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def hardDeletetechnical(id:int, db:db_dependency):
    return hardDelete_technical_service(id,db)
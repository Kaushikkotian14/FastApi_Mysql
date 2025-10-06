
from pydantic import BaseModel

class getworkExperienceByIdSchema(BaseModel):
    workExperienceId:int
    userId:int
    firstname:str
    lastname:str
    currentEmployer: str 
    totalYears: int
    personalInfoId: int 
    
   
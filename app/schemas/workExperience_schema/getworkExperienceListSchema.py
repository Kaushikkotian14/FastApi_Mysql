from pydantic import BaseModel

class getworkExperienceListSchema(BaseModel):
    currentEmployer: str 
    totalYears: int
    personalInfoId: int 
    
   
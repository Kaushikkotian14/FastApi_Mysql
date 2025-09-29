from pydantic import BaseModel

class createWorkExperience(BaseModel):
    currentEmployer: str 
    totalYears: int
    personalInfoId: int 
    
   
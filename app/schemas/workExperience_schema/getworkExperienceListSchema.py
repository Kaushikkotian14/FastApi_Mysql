from pydantic import BaseModel

class getworkExperienceListSchema(BaseModel):
    firstname:str
    lastname:str
    currentEmployer: str 
    totalYears: int
    
   
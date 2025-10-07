from pydantic import BaseModel

class getPersonalInfoListSchema(BaseModel):
    firstname:str
    lastname:str
    professionalTitle: str 
    company: str 
    department: str
   
    


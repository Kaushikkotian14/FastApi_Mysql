from pydantic import BaseModel

class getPersonalInfoByIdSchema(BaseModel):
    personalInfoId:int
    firstname:str
    lastname:str
    professionalTitle: str 
    company: str 
    department: str
    userId: int 
    


from pydantic import BaseModel

class getPersonalInfoListSchema(BaseModel):
    professionalTitle: str 
    company: str 
    department: str
    userId: int 
    


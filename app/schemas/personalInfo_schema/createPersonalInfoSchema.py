from pydantic import BaseModel

class createPersonalInfo(BaseModel):
    professionalTitle: str 
    company: str 
    department: str
    userId: int 
    

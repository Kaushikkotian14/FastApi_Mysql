from pydantic import BaseModel

class getUserByIdUserSchema(BaseModel):
    userId:int
    firstname: str 
    lastname: str 
    phoneNumber: str
    age: int 
    
    

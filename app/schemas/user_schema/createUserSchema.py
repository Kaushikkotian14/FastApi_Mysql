from pydantic import BaseModel


class createUser(BaseModel):
    firstname: str 
    lastname: str 
    phoneNumber: str
    age: int 
    

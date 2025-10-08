from pydantic import BaseModel

class getUserUsersListSchema(BaseModel):
    firstname: str 
    lastname: str 
    phoneNumber: str
    age: int 
    
    

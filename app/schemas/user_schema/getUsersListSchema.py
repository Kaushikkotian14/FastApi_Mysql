from pydantic import BaseModel

class getUserUsersListSchema(BaseModel):
    firstName: str 
    lastName: str 
    phoneNumber: str
    age: int 
    
    

from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class createUser(BaseModel):
    firstname: str 
    lastname: str 
    phoneNumber: str
    age: int 
    

class userResponse(BaseModel): # This is the class you should use as a return type
    firstname: str 
    lastname: str 
    phoneNumber: str
    age: int 

class UserUpdate(BaseModel):
    firstname: Optional[str] 
    lastname: Optional[str] 
    phoneNumber: Optional[str]
    age: Optional[int]
    is_active: Optional[bool] 
    changed_by: Optional[int]
    deleted_by: Optional[int] = None
    deleted_at: Optional[datetime] = None
from typing import Optional
from pydantic import BaseModel

class UserUpdate(BaseModel):
    firstname: Optional[str] 
    lastname: Optional[str] 
    phoneNumber: Optional[str]
    age: Optional[int]
    is_active: Optional[bool] 
    changed_by: Optional[int]
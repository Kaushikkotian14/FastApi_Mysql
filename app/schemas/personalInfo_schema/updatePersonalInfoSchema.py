from typing import Optional
from pydantic import BaseModel

class updatePersonalInfo(BaseModel):
    professionalTitle: Optional[str] 
    company: Optional[str] 
    department: Optional[str]
    userId: Optional[int]
    is_active: Optional[bool] 


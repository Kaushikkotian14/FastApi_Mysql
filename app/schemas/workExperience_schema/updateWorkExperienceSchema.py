from typing import Optional
from pydantic import BaseModel

class updateWorkExperience(BaseModel):
    currentEmployer: Optional[str] 
    totalYears: Optional[int] 
    personalInfoId: Optional[int]
    is_active: Optional[bool] 


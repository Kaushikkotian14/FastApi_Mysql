from typing import Optional
from pydantic import BaseModel

class updateWorkExperience(BaseModel):
    currentEmployer: Optional[str] 
    totalYears: Optional[int] 
    personalInfoIderId: Optional[int]
    is_active: Optional[bool] 
    changed_by: int


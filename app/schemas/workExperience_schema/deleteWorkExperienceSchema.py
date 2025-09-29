from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class deleteWorkExperience(BaseModel):   
    is_active: Optional[bool] 
    deleted_by: int
    deleted_at:datetime



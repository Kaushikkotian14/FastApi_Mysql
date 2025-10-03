from typing import Optional
from pydantic import BaseModel

class updateTechnicalSchema(BaseModel):
    category: Optional[str] 
    skillId: Optional[int]
    is_active: Optional[bool] 


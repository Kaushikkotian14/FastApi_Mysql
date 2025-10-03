from pydantic import BaseModel
from typing import Optional

class updateProficiencynameSchema(BaseModel):
    name: Optional[str] 
    proficiency_rating: Optional[int]
    is_active:Optional[bool]
    
   
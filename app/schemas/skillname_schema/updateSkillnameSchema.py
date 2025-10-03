from pydantic import BaseModel
from typing import Optional

class updateSkillnameSchema(BaseModel):
    name: Optional[str] 
    is_active:Optional[bool]
    
   
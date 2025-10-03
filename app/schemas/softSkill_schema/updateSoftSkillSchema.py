from typing import Optional
from pydantic import BaseModel

class updateSoftSkillSchema(BaseModel):
    skillLevel: Optional[str] 
    skill: Optional[str]
    experience:Optional[str]
    skillId: Optional[int] 
    is_active: Optional[bool] 


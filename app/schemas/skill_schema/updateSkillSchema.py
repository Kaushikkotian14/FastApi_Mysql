from pydantic import BaseModel
from typing import Optional

class updateSkillSchema(BaseModel):
    workExperienceId: Optional[int] 
    is_active: Optional[bool]

    
   
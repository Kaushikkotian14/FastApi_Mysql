from pydantic import BaseModel
from typing import Optional

class updateSkillnameMappingSchema(BaseModel):
    technicalId: Optional[int] 
    proficiencyId: Optional[int]
    is_active: Optional[bool]

    
   
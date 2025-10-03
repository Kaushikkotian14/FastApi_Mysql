from pydantic import BaseModel
from typing import Optional

class updateProficiencynameMappingSchema(BaseModel):
    technicalId: Optional[int]
    proficiencyId: Optional[int]
    is_active: Optional[bool]

    
   
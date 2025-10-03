from pydantic import BaseModel

class createSkillnameMappingSchema(BaseModel):
    technicalId: int 
    skillnameId: int

    
   
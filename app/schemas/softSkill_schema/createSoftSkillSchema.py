from pydantic import BaseModel

class createSoftSkillSchema(BaseModel):
    skillLevel: str 
    skill: str
    experience:str
    skillId: int 
    
   
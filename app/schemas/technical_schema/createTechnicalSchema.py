from pydantic import BaseModel

class createTechnicalSchema(BaseModel):
    category: str 
    skillId: int

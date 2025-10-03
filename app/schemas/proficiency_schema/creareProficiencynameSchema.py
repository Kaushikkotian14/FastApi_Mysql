from pydantic import BaseModel

class createProficiencynameSchema(BaseModel):
    name: str 
    proficiency_rating: int

    
   
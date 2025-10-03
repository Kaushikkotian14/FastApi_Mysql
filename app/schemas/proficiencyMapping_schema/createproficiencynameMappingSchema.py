from pydantic import BaseModel

class createProficiencynameMappingSchema(BaseModel):
    technicalId: int 
    proficiencyId: int

    
   
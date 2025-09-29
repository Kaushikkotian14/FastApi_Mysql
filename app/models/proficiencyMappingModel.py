from datetime import datetime
from uuid import UUID,uuid4
from sqlalchemy import Column, Integer, String,Boolean,DateTime,UUID,ForeignKey
from database.db import base
from sqlalchemy.orm import relationship


class proficiencyMappingModel(base):
    __tablename__ = "proficiencymapping"
    proficiencyMapping = Column(Integer, primary_key=True, index=True)
    technicalId = Column(Integer, ForeignKey("technical.technicalId"))
    proficiencyId = Column(Integer, ForeignKey("proficiency.proficiencyId"))
    is_active = Column(Boolean,default=True)
    created_by = Column(Integer,ForeignKey("user.userId"),default = 1,nullable=False)
    created_at = Column(DateTime,default = datetime.now(),nullable=False)
    changed_by = Column(Integer,ForeignKey("user.userId"),default = None)
    changed_at = Column(DateTime,default = None)
    deleted_by = Column(Integer,ForeignKey("user.userId"),default = None)
    deleted_at = Column(DateTime,default = None)
    uniqueIdentifier = Column(UUID,default =uuid4()) 
    version = Column(DateTime,default = datetime.now())

    # technical = relationship("technical", back_populates="proficiencyMapping")
    # proficiency = relationship("proficiency", back_populates="proficiencyMapping")
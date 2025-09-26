from datetime import datetime
from uuid import UUID
from sqlalchemy import Column, Integer, String,Boolean,DateTime,UUID,ForeignKey
from database.db import base
from sqlalchemy.orm import relationship


class proficiencyMappingModel(base):
    __tablename__ = "proficiencymapping"
    proficiencyMapping = Column(Integer, primary_key=True, index=True)
    technicalId = Column(Integer, ForeignKey("technicalModel.technicalId"))
    proficiencyId = Column(Integer, ForeignKey("proficiencyModel.proficiencyId"))
    is_active = Column(Boolean,default=True)
    created_by = Column(Integer,default = 1,nullable=False)
    created_at = Column(DateTime,default = datetime.now(),nullable=False)
    changed_by = Column(Integer,default = None)
    changed_at = Column(DateTime,default = None)
    deleted_by = Column(Integer,default = None)
    deleted_at = Column(DateTime,default = None)
    uniqueIdentifier = Column(UUID,nullable=False) 
    version = Column(DateTime,default = datetime.now())

    # technical = relationship("technical", back_populates="proficiencyMapping")
    # proficiency = relationship("proficiency", back_populates="proficiencyMapping")
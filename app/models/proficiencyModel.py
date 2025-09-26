from datetime import datetime
from uuid import UUID
from sqlalchemy import Column, Integer, String,Boolean,DateTime,UUID,ForeignKey
from database.db import base
from sqlalchemy.orm import relationship


class proficiencyModel(base):
    __tablename__ = "proficiency"
    proficiencyId = Column(Integer, primary_key=True, index=True)
    name = Column(String(255),nullable=False)
    is_active = Column(Boolean,default=True)
    created_by = Column(Integer,default = 1,nullable=False)
    created_at = Column(DateTime,default = datetime.now(),nullable=False)
    changed_by = Column(Integer,default = None)
    changed_at = Column(DateTime,default = None)
    deleted_by = Column(Integer,default = None)
    deleted_at = Column(DateTime,default = None)
    uniqueIdentifier = Column(UUID,nullable=False) 
    version = Column(DateTime,default = datetime.now())

  
    # proficiencymapping = relationship("proficiencymapping", back_populates="proficiency")
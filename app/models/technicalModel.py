from datetime import datetime
from uuid import UUID,uuid4
from sqlalchemy import Column, Integer, String,Boolean,DateTime,UUID,ForeignKey
from database.db import base
from sqlalchemy.orm import relationship


class technicalModel(base):
    __tablename__ = "technical"
    technicalId = Column(Integer, primary_key=True, index=True)
    skillId = Column(Integer, ForeignKey("skill.skillId"))
    category = Column(String(255),nullable=False)
    is_active = Column(Boolean,default=True)
    created_by = Column(Integer,ForeignKey("user.userId"),default = 1,nullable=False)
    created_at = Column(DateTime,default = datetime.now(),nullable=False)
    changed_by = Column(Integer,ForeignKey("user.userId"),default = None)
    changed_at = Column(DateTime,default = None)
    deleted_by = Column(Integer,ForeignKey("user.userId"),default = None)
    deleted_at = Column(DateTime,default = None)
    uniqueIdentifier = Column(UUID,default =uuid4()) 
    version = Column(DateTime,default = datetime.now())


    # skill = relationship("skillId", back_populates="technical")
    # skillnamemapping = relationship("skillnamemapping", back_populates="technical")
    # proficiencymapping = relationship("proficiencymapping", back_populates="technical")

from datetime import datetime
from uuid import UUID,uuid4
from sqlalchemy import Column, Integer, String,Boolean,DateTime,UUID,ForeignKey
from database.db import base
from sqlalchemy.orm import relationship


class skillModel(base):
    __tablename__ = "skill"
    skillId = Column(Integer, primary_key=True, index=True)
    workExperienceId = Column(Integer, ForeignKey("workExperience.workExperienceId"))
    is_active = Column(Boolean,default=True)
    created_by = Column(Integer,ForeignKey("user.userId"),default = 1,nullable=False)
    created_at = Column(DateTime,default = datetime.now(),nullable=False)
    changed_by = Column(Integer,ForeignKey("user.userId"),default = None)
    changed_at = Column(DateTime,default = None)
    deleted_by = Column(Integer,ForeignKey("user.userId"),default = None)
    deleted_at = Column(DateTime,default = None)
    uniqueIdentifier = Column(UUID,default =uuid4()) 
    version = Column(DateTime,default = datetime.now())
    
    # technical = relationship("technical", back_populates="skill")
    # soft = relationship("soft", back_populates="skill")
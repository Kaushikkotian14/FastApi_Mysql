from datetime import datetime
from uuid import UUID,uuid4
from sqlalchemy import Column, Integer, String,Boolean,DateTime,UUID,ForeignKey
from database.db import base
from sqlalchemy.orm import relationship



class softModel(base):
    __tablename__ = "soft"
    softId = Column(Integer, primary_key=True, index=True)
    skillId = Column(Integer, ForeignKey("skill.skillId"))
    skill = Column(String(255),nullable=False)
    skillLevel = Column(String(255),nullable=False)
    experience = Column(String(255),nullable=False)
    is_active = Column(Boolean,default=True)
    created_by = Column(Integer,ForeignKey("user.userId"),default = 1,nullable=False)
    created_at = Column(DateTime,default = datetime.now(),nullable=False)
    changed_by = Column(Integer,ForeignKey("user.userId"),default = None)
    changed_at = Column(DateTime,default = None)
    deleted_by = Column(Integer,ForeignKey("user.userId"),default = None)
    deleted_at = Column(DateTime,default = None)
    uniqueIdentifier = Column(UUID,default =uuid4()) 
    version = Column(DateTime,default = datetime.now())
    
    soft_skill = relationship("skillModel",foreign_keys=[skillId], back_populates="skill_soft")

    soft_user_created_by = relationship("userModel",foreign_keys=[created_by ], back_populates="user_soft_created_by")
    soft_user_changed_by = relationship("userModel",foreign_keys=[changed_by ], back_populates="user_soft_changed_by")
    soft_user_deleted_by = relationship("userModel",foreign_keys=[deleted_by], back_populates="user_soft_deleted_by")
from datetime import datetime
from uuid import UUID,uuid4
from sqlalchemy import Column, Integer, String,Boolean,DateTime,UUID,ForeignKey
from database.db import base
from sqlalchemy.orm import relationship


class skillnameModel(base):
    __tablename__ = "skillname"
    skillnameId = Column(Integer, primary_key=True, index=True)
    name = Column(String(255),nullable=False)
    is_active = Column(Boolean,default=True)
    created_by = Column(Integer,ForeignKey("user.userId"),default = 1,nullable=False)
    created_at = Column(DateTime,default = datetime.now(),nullable=False)
    changed_by = Column(Integer,ForeignKey("user.userId"),default = None)
    changed_at = Column(DateTime,default = None)
    deleted_by = Column(Integer,ForeignKey("user.userId"),default = None)
    deleted_at = Column(DateTime,default = None)
    uniqueIdentifier = Column(UUID,default =uuid4()) 
    version = Column(DateTime,default = datetime.now())
 
    skillname_skillnamemapping = relationship("skillnamemappingModel",foreign_keys="[skillnamemappingModel.skillnameId]", back_populates="skillnamemapping_skillname")
  
    skillname_user_created_by = relationship("userModel",foreign_keys=[created_by ], back_populates="user_skillname_created_by")
    skillname_user_changed_by = relationship("userModel",foreign_keys=[changed_by ], back_populates="user_skillname_changed_by")
    skillname_user_deleted_by = relationship("userModel",foreign_keys=[deleted_by], back_populates="user_skillname_deleted_by")
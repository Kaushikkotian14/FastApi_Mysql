from datetime import datetime
from uuid import UUID,uuid4
from sqlalchemy import Column, Integer, String,Boolean,DateTime,UUID,ForeignKey
from database.db import base
from sqlalchemy.orm import relationship


class proficiencyModel(base):
    __tablename__ = "proficiency"
    proficiencyId = Column(Integer, primary_key=True, index=True)
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

  
    proficiency_proficiencymapping = relationship("proficiencymappingModel",foreign_keys="[proficiencymappingModel.proficiencyId]", back_populates="proficiencymapping_proficiency")
  
    proficiency_user_created_by = relationship("userModel",foreign_keys=[created_by ], back_populates="user_proficiency_created_by")
    proficiency_user_changed_by = relationship("userModel",foreign_keys=[changed_by ], back_populates="user_proficiency_changed_by")
    proficiency_user_deleted_by = relationship("userModel",foreign_keys=[deleted_by], back_populates="user_proficiency_deleted_by")
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


    technical_skill = relationship("skillModel",foreign_keys=[skillId], back_populates="skill_technical")

    technical_user_created_by = relationship("userModel",foreign_keys=[created_by ], back_populates="user_technical_created_by")
    technical_user_changed_by = relationship("userModel",foreign_keys=[changed_by ], back_populates="user_technical_changed_by")
    technical_user_deleted_by = relationship("userModel",foreign_keys=[deleted_by], back_populates="user_technical_deleted_by")

    technical_skillnamemapping = relationship("skillnamemappingModel",foreign_keys="[skillnamemappingModel.technicalId]", back_populates="skillnamemapping_technical")
    technical_proficiencymapping = relationship("proficiencymappingModel",foreign_keys="[proficiencymappingModel.technicalId]", back_populates="proficiencymapping_technical")
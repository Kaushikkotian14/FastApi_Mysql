from datetime import datetime
from uuid import UUID,uuid4
from sqlalchemy import Column, Integer, String,Boolean,DateTime,UUID,ForeignKey
from database.db import base
from sqlalchemy.orm import relationship


class skillModel(base):
    __tablename__ = "skill"
    skillId = Column(Integer, primary_key=True, index=True)
    workExperienceId = Column(Integer, ForeignKey("workExperience.workExperienceId"),unique=True)
    is_active = Column(Boolean,default=True)
    created_by = Column(Integer,ForeignKey("user.userId"),default = 1,nullable=False)
    created_at = Column(DateTime,default = datetime.now(),nullable=False)
    changed_by = Column(Integer,ForeignKey("user.userId"),default = None)
    changed_at = Column(DateTime,default = None)
    deleted_by = Column(Integer,ForeignKey("user.userId"),default = None)
    deleted_at = Column(DateTime,default = None)
    uniqueIdentifier = Column(UUID,default =uuid4()) 
    version = Column(DateTime,default = datetime.now())

    skill_workExperience = relationship("workExperienceModel",foreign_keys=[workExperienceId], back_populates="workExperience_skill")

    skill_user_created_by = relationship("userModel",foreign_keys=[created_by ], back_populates="user_skill_created_by")
    skill_user_changed_by = relationship("userModel",foreign_keys=[changed_by ], back_populates="user_skill_changed_by")
    skill_user_deleted_by = relationship("userModel",foreign_keys=[deleted_by], back_populates="user_skill_deleted_by")


    skill_technical = relationship("technicalModel",foreign_keys="[technicalModel.skillId]", back_populates="technical_skill")
    skill_soft = relationship("softModel",foreign_keys="[softModel.skillId]", back_populates="soft_skill")
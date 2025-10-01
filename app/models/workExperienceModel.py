from datetime import datetime
from uuid import UUID,uuid4
from sqlalchemy import Column, Integer, String,Boolean,DateTime,UUID,ForeignKey
from database.db import base
from sqlalchemy.orm import relationship


class workExperienceModel(base):
    __tablename__ = "workExperience"
    workExperienceId = Column(Integer, primary_key=True, index=True)
    personalInfoId = Column(Integer, ForeignKey("personalInfo.personalInfoId"),unique=True)
    currentEmployer = Column(String(255),nullable=False)
    totalYears= Column(Integer,nullable=False)
    is_active = Column(Boolean,default=True)
    created_by = Column(Integer,ForeignKey("user.userId"),default = 1,nullable=False)
    created_at = Column(DateTime,default = datetime.now(),nullable=False)
    changed_by = Column(Integer,ForeignKey("user.userId"),default = None)
    changed_at = Column(DateTime,default = None)
    deleted_by = Column(Integer,ForeignKey("user.userId"),default = None)
    deleted_at = Column(DateTime,default = None)
    uniqueIdentifier = Column(UUID,default =uuid4()) 
    version = Column(DateTime,default = datetime.now())
    
    workExperience_personalInfo = relationship("personalInfoModel",foreign_keys=[personalInfoId], back_populates="personalInfo_workExperience")

    workExperience_user_created_by = relationship("userModel",foreign_keys=[created_by ], back_populates="user_workExperience_created_by")
    workExperience_user_changed_by = relationship("userModel",foreign_keys=[changed_by ], back_populates="user_workExperience_changed_by")
    workExperience_user_deleted_by = relationship("userModel",foreign_keys=[deleted_by], back_populates="user_workExperience_deleted_by")

    workExperience_skill = relationship("skillModel",foreign_keys="[skillModel.workExperienceId]", back_populates="skill_workExperience")
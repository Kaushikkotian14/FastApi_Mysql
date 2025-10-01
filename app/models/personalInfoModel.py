from datetime import datetime
from uuid import UUID,uuid4
from sqlalchemy import Column, Integer, String,Boolean,DateTime,UUID,ForeignKey
from database.db import base
from sqlalchemy.orm import relationship


class personalInfoModel(base):
    __tablename__ = "personalInfo"
    personalInfoId = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, ForeignKey("user.userId"),unique=True)
    professionalTitle = Column(String(255),nullable=False)
    company= Column(String(255),nullable=False)
    department = Column(String(15),nullable=False)
    is_active = Column(Boolean,default=True)
    created_by = Column(Integer, ForeignKey("user.userId"),default = 1,nullable=False)
    created_at = Column(DateTime,default = datetime.now(),nullable=False)
    changed_by = Column(Integer, ForeignKey("user.userId"),default = None)
    changed_at = Column(DateTime,default = None)
    deleted_by = Column(Integer,ForeignKey("user.userId"),default = None)
    deleted_at = Column(DateTime,default = None)
    uniqueIdentifier = Column(UUID,default =uuid4())  
    version = Column(DateTime,default = datetime.now())

    personalInfo_user = relationship("userModel",foreign_keys=[userId], back_populates="user_personalInfo")
    
    personalInfo_user_created_by = relationship("userModel",foreign_keys=[created_by ], back_populates="user_personalInfo_created_by")
    personalInfo_user_changed_by = relationship("userModel",foreign_keys=[changed_by ], back_populates="user_personalInfo_changed_by")
    personalInfo_user_deleted_by = relationship("userModel",foreign_keys=[deleted_by], back_populates="user_personalInfo_deleted_by")
    
    personalInfo_workExperience = relationship("workExperienceModel",foreign_keys="[workExperienceModel.personalInfoId]", back_populates="workExperience_personalInfo")
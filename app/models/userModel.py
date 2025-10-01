from datetime import datetime
from uuid import UUID,uuid4
from sqlalchemy import Column, Integer, String,Boolean,DateTime,UUID
from database.db import base
from sqlalchemy.orm import relationship


class userModel(base):
    __tablename__ = "user"
    userId = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(255),nullable=False,index=True)
    lastname= Column(String(255),nullable=False,index=True)
    phoneNumber = Column(String(15),nullable=False)
    age = Column(Integer,nullable=False)
    is_active = Column(Boolean,default=True)
    created_by = Column(Integer,default = 1,nullable=False)
    created_at = Column(DateTime,default = datetime.now(),nullable=False)
    changed_by = Column(Integer,default = None)
    changed_at = Column(DateTime,default = None)
    deleted_by = Column(Integer,default = None)
    deleted_at = Column(DateTime,default = None)
    uniqueIdentifier = Column(UUID,default =uuid4()) 
    version = Column(DateTime,default = datetime.now())
    
    user_personalInfo = relationship("personalInfoModel",foreign_keys="[personalInfoModel.userId]", back_populates="personalInfo_user")
    user_personalInfo_created_by = relationship("personalInfoModel",foreign_keys="[personalInfoModel.created_by]",back_populates="personalInfo_user_created_by")
    user_personalInfo_changed_by = relationship("personalInfoModel", foreign_keys="[personalInfoModel.changed_by]",back_populates="personalInfo_user_changed_by")
    user_personalInfo_deleted_by = relationship("personalInfoModel", foreign_keys="[personalInfoModel.deleted_by]",back_populates="personalInfo_user_deleted_by")

    user_workExperience_created_by = relationship("workExperienceModel",foreign_keys="[workExperienceModel.created_by]",back_populates="workExperience_user_created_by")
    user_workExperience_changed_by = relationship("workExperienceModel", foreign_keys="[workExperienceModel.changed_by]",back_populates="workExperience_user_changed_by")
    user_workExperience_deleted_by = relationship("workExperienceModel", foreign_keys="[workExperienceModel.deleted_by]",back_populates="workExperience_user_deleted_by")

    user_skill_created_by = relationship("skillModel",foreign_keys="[skillModel.created_by]",back_populates="skill_user_created_by")
    user_skill_changed_by = relationship("skillModel", foreign_keys="[skillModel.changed_by]",back_populates="skill_user_changed_by")
    user_skill_deleted_by = relationship("skillModel", foreign_keys="[skillModel.deleted_by]",back_populates="skill_user_deleted_by")

    user_technical_created_by = relationship("technicalModel",foreign_keys="[technicalModel.created_by]",back_populates="technical_user_created_by")
    user_technical_changed_by = relationship("technicalModel", foreign_keys="[technicalModel.changed_by]",back_populates="technical_user_changed_by")
    user_technical_deleted_by = relationship("technicalModel", foreign_keys="[technicalModel.deleted_by]",back_populates="technical_user_deleted_by")

    user_soft_created_by = relationship("softModel",foreign_keys="[softModel.created_by]",back_populates="soft_user_created_by")
    user_soft_changed_by = relationship("softModel", foreign_keys="[softModel.changed_by]",back_populates="soft_user_changed_by")
    user_soft_deleted_by = relationship("softModel", foreign_keys="[softModel.deleted_by]",back_populates="soft_user_deleted_by")

    user_skillnamemapping_created_by = relationship("skillnamemappingModel",foreign_keys="[skillnamemappingModel.created_by]",back_populates="skillnamemapping_user_created_by")
    user_skillnamemapping_changed_by = relationship("skillnamemappingModel", foreign_keys="[skillnamemappingModel.changed_by]",back_populates="skillnamemapping_user_changed_by")
    user_skillnamemapping_deleted_by = relationship("skillnamemappingModel", foreign_keys="[skillnamemappingModel.deleted_by]",back_populates="skillnamemapping_user_deleted_by")

    user_proficiencymapping_created_by = relationship("proficiencymappingModel",foreign_keys="[proficiencymappingModel.created_by]",back_populates="proficiencymapping_user_created_by")
    user_proficiencymapping_changed_by = relationship("proficiencymappingModel", foreign_keys="[proficiencymappingModel.changed_by]",back_populates="proficiencymapping_user_changed_by")
    user_proficiencymapping_deleted_by = relationship("proficiencymappingModel", foreign_keys="[proficiencymappingModel.deleted_by]",back_populates="proficiencymapping_user_deleted_by")

    user_skillname_created_by = relationship("skillnameModel",foreign_keys="[skillnameModel.created_by]",back_populates="skillname_user_created_by")
    user_skillname_changed_by = relationship("skillnameModel", foreign_keys="[skillnameModel.changed_by]",back_populates="skillname_user_changed_by")
    user_skillname_deleted_by = relationship("skillnameModel", foreign_keys="[skillnameModel.deleted_by]",back_populates="skillname_user_deleted_by")

    user_proficiency_created_by = relationship("proficiencyModel",foreign_keys="[proficiencyModel.created_by]",back_populates="proficiency_user_created_by")
    user_proficiency_changed_by = relationship("proficiencyModel", foreign_keys="[proficiencyModel.changed_by]",back_populates="proficiency_user_changed_by")
    user_proficiency_deleted_by = relationship("proficiencyModel", foreign_keys="[proficiencyModel.deleted_by]",back_populates="proficiency_user_deleted_by")
    
    user_register = relationship("registerModel",foreign_keys="[registerModel.userId]", back_populates="register_user")
    user_register_created_by = relationship("registerModel",foreign_keys="[registerModel.created_by]",back_populates="register_user_created_by")
    user_register_changed_by = relationship("registerModel", foreign_keys="[registerModel.changed_by]",back_populates="register_user_changed_by")
    user_register_deleted_by = relationship("registerModel", foreign_keys="[registerModel.deleted_by]",back_populates="register_user_deleted_by")


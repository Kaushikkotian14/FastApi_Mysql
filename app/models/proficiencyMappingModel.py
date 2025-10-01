from datetime import datetime
from uuid import UUID,uuid4
from sqlalchemy import Column, Integer, String,Boolean,DateTime,UUID,ForeignKey
from database.db import base
from sqlalchemy.orm import relationship


class proficiencymappingModel(base):
    __tablename__ = "proficiencymapping"
    proficiencymappingId = Column(Integer, primary_key=True, index=True)
    technicalId = Column(Integer, ForeignKey("technical.technicalId"))
    proficiencyId = Column(Integer, ForeignKey("proficiency.proficiencyId"))
    is_active = Column(Boolean,default=True)
    created_by = Column(Integer,ForeignKey("user.userId"),default = 1,nullable=False)
    created_at = Column(DateTime,default = datetime.now(),nullable=False)
    changed_by = Column(Integer,ForeignKey("user.userId"),default = None)
    changed_at = Column(DateTime,default = None)
    deleted_by = Column(Integer,ForeignKey("user.userId"),default = None)
    deleted_at = Column(DateTime,default = None)
    uniqueIdentifier = Column(UUID,default =uuid4()) 
    version = Column(DateTime,default = datetime.now())

    proficiencymapping_technical = relationship("technicalModel",foreign_keys=[technicalId], back_populates="technical_proficiencymapping")

    proficiencymapping_user_created_by = relationship("userModel",foreign_keys=[created_by ], back_populates="user_proficiencymapping_created_by")
    proficiencymapping_user_changed_by = relationship("userModel",foreign_keys=[changed_by ], back_populates="user_proficiencymapping_changed_by")
    proficiencymapping_user_deleted_by = relationship("userModel",foreign_keys=[deleted_by], back_populates="user_proficiencymapping_deleted_by")

    proficiencymapping_proficiency = relationship("proficiencyModel",foreign_keys=[proficiencyId], back_populates="proficiency_proficiencymapping")
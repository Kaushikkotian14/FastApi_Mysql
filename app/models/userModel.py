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
    
    # personalInfo = relationship("personalInfo", back_populates="user")










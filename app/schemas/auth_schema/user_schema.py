from fastapi import HTTPException
from pydantic import BaseModel, field_validator
import re

class userSchema(BaseModel):
    email: str
    password:str
    userId:int

    @field_validator("email")
    def validate_email(cls, v):
        if " " in v:
            raise ValueError("Email must not contain spaces")
        #    raise HTTPException(status_code=400,detail="Email must not contain spaces")
        
        emailRegex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(emailRegex, v):
            raise ValueError("Email is not in proper format")
            # raise HTTPException(status_code=400,detail="Email is not in proper format")
        return v
 
    @field_validator("password")
    def validate_password(cls, v):
        if " " in v:
            raise ValueError("Password must not contain spaces")
            # raise HTTPException(status_code=400,detail="Password must not contain spaces")
        
        passwordRegex = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>/?]).*$'
        if not re.match(passwordRegex, v):
            raise ValueError("Password must contain at least one uppercase, one lowercase,one digit and one special character")
            # raise HTTPException(status_code=400,detail="Password must contain at least one uppercase, one lowercase,one digit and one special character")
        return v
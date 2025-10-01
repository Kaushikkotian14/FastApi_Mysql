from pydantic import BaseModel
from typing import Optional

class userSchema(BaseModel):
    email: str
    password:str
    userId:int
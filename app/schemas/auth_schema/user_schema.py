from pydantic import BaseModel
from typing import Optional

class userSchema(BaseModel):
    email: str
    password:Optional[str]
    userId:int
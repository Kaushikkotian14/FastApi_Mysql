from fastapi import Depends, HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from jose import  JWTError
from utils.token import SECRET_KEY, ALGORITHM
from schemas.auth_schema.user_schema import userSchema
from schemas.auth_schema.token_schema import tokenSchema
from  schemas.auth_schema.user_schema import userSchema
from models.registerModel import registerModel
from utils.token import verify_password,jwt_decode

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def authenticate_user(email:str,password:str,db):
    
    user = db.query(registerModel).filter(registerModel.email == email).first()
    if not user:
        return False
    if not verify_password(password,user.password):
        return False
    return user

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt_decode(token)
        email: str = payload.get("sub")
        userId:int = payload.get("userId")
        password:str = payload.get("password")
        if email is None or userId is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid User")
        user = userSchema(email=email,userId=userId,password=password)
        return user
    except JWTError:
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid User")
    

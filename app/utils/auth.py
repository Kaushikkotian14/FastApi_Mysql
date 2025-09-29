from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from utils.token import SECRET_KEY, ALGORITHM
from schemas.token_schema import TokenData
 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
 
async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        token_data = TokenData(username=username)
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"username": token_data.username}

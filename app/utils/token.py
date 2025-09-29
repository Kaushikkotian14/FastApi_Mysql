from jose import jwt
from datetime import datetime, timedelta, timezone
import secrets
 
SECRET_KEY = secrets.token_urlsafe(32)
ALGORITHM = "HS256"
 
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=30))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
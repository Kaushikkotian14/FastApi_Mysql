from repositories.auth_repo import create_user_repo
from models.registerModel import registerModel
from utils.token import get_password_hash
from schemas.auth_schema.user_schema import userSchema

def create_user_service(createUser,db):
    user = userSchema(
        email=createUser.email,
        password=get_password_hash(createUser.password),
        userId=createUser.userId
    )
    create_User = registerModel(**user.model_dump())
    create_user_repo(create_User,db)
    return {"msg": "user registered"}
from models.userModel import userModel


def user_data_by_id_repo(userId,db):
    userData=db.query(userModel).filter(userModel.userId == userId).first()
    return userData

def get_users_repo(db):
    usersData=db.query(userModel).all()
    return usersData

def add_user_repo(userData,db):
    db.add(userData)
    db.commit()
    db.refresh(userData)

def update_user_repo(userData,db):
    db.commit()
    db.refresh(userData)
    
def delete_user_repo(userData,db):
    db.commit()
    db.refresh(userData)
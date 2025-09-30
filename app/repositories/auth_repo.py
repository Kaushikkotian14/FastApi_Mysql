
def create_user_repo(create_User,db):
    db.add(create_User)
    db.commit()
    db.refresh(create_User)
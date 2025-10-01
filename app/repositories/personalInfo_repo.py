from models.personalInfoModel import personalInfoModel


def personalInfo_by_id_repo(personalInfoId,db):
    personalInfo=db.query(personalInfoModel).filter(personalInfoModel.personalInfoId == personalInfoId).first()
    return personalInfo

def get_personalInfos_repo(db):
    personalInfo=db.query(personalInfoModel).filter(personalInfoModel.deleted_by == None).all()
    return personalInfo

def add_personalInfo_repo(personalInfo,db):
    db.add(personalInfo)
    db.commit()
    db.refresh(personalInfo)

def update_personalInfo_repo(personalInfo,db):
    db.commit()
    db.refresh(personalInfo)
    
def delete_personalInfo_repo(personalInfo,db):
    db.commit()
    db.refresh(personalInfo)
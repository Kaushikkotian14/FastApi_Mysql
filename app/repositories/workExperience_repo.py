from models.workExperienceModel import workExperienceModel


def workExperience_by_id_repo(workExperienceId,db):
    workExperience=db.query(workExperienceModel).filter(workExperienceModel.workExperienceId == workExperienceId).first()
    return workExperience

def get_workExperiences_repo(db):
    workExperience=db.query(workExperienceModel).filter(workExperienceModel.deleted_by == None).all()
    return workExperience

def add_workExperience_repo(workExperience,db):
    db.add(workExperience)
    db.commit()
    db.refresh(workExperience)

def update_workExperience_repo(workExperience,db):
    db.commit()
    db.refresh(workExperience)
    
def delete_workExperience_repo(workExperience,db):
    db.commit()
    db.refresh(workExperience)
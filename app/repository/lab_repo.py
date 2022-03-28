from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.schema import schema
from app.models import models


def create(request: schema.Lab, db: Session):
    new_lab = models.Lab(
        institute_id=request.institute_id,
        lab_admin_name=request.lab_admin_name,
        lab_name=request.lab_name,
        lab_description=request.lab_description,
        lab_address=request.lab_address,
        longitude=request.longitude,
        latitude=request.latitude,
        lab_student_capacity=request.lab_student_capacity
    )
    db.add(new_lab)
    institute=db.query(models.Institute).filter(models.Institute.institute_id==request.institute_id).first()
    institute.labs.append(new_lab)
    db.commit()
    db.refresh(new_lab)
    return new_lab


def show(id: int, db: Session):
    lab=db.query(models.Lab).filter(models.Lab.lab_id==id).first()
    if not lab:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Lab with the id {id} is not found")
    return lab

def show_all_labs(db:Session):
    labs=db.query(models.Lab).all()
    return labs

def delete(id,db:Session):
    lab=db.query(models.Lab).filter(models.Lab.lab_id==id).first()
    db.delete(lab)
    db.commit()
    
    
# def show_experiments_from_lab_id(lab_id:int, db: Session):
#     all_experiments=db.query(models.lab_experiments).all()
#     lab_id=int(lab_id)
#     experiments=[]
#     for experiment in all_experiments:
#         if experiment.lab_id==lab_id:
#             experiment_temp=db.query(models.Experiment).filter(models.Experiment.experiment_id==experiment.experiment_id).first()
#             experiments.append(experiment_temp)
#     return experiments        
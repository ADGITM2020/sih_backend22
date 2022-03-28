from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.schema import schema
from app.models import models
from app.routes import equipment


def create(request: schema.Experiment, db: Session):
    new_experiment = models.Experiment(
        aim=request.aim,
        description=request.description,
    )

    if request.equipments is not None:
        for equipment_id in request.equipments:
            equipment = db.query(models.Equipment).filter(
                models.Equipment.equipment_id == equipment_id).first()
            equipment.experiments.append(new_experiment)
            new_experiment.equipments.append(equipment)

    db.add(new_experiment)
    db.commit()
    db.refresh(new_experiment)
    return new_experiment


def show(id: int, db: Session):
    experiment = db.query(models.Experiment).filter(
        models.Experiment.experiment_id == id).first()
    if not experiment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Experiment with the id {id} is not found")
    return experiment

def show_equipments_from_experiment_id(experiment_id:int, db: Session):
    all_equipments=db.query(models.experiment_equipments).all()
    experiment_id=int(experiment_id)
    equipments=[]
    for equipment in all_equipments:
        if equipment.experiment_id==experiment_id:
            equipments.append(equipment)
    return equipments        
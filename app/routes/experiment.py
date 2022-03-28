from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.models import models
from app.config import database
from app.schema import schema
from app.repository import experiment_repo
from typing import List

router = APIRouter(
    prefix="/experiment",
    tags=['Experiment']
)

get_db = database.get_db


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_experiment(request: schema.Experiment, db: Session = Depends(get_db)):
    return experiment_repo.create(request, db)


@router.get("/{id}", status_code=status.HTTP_200_OK)
def show_experiment(id, db: Session = Depends(get_db)):
    return experiment_repo.show(id, db)

@router.get("/{experiment_id}/equipments", status_code=status.HTTP_200_OK)
def show_equipment_from_exp_id(id, db: Session = Depends(get_db)):
    return experiment_repo.show_equipments_from_experiment_id(id, db)


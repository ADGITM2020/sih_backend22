from fastapi import APIRouter, Depends,status,Response
from sqlalchemy.orm import Session
from app.config import database
from app.schema import schema
from app.repository import lab_repo
from typing import List

router=APIRouter(
    prefix="/lab",
    tags=['Lab']
)

get_db=database.get_db

@router.post("/",response_model=schema.ShowLab,status_code=status.HTTP_201_CREATED)
def create_lab(request:schema.Lab,db:Session=Depends(get_db)):
    return lab_repo.create(request,db)

@router.get("/",status_code=status.HTTP_200_OK,response_model=List[schema.ShowLab])
def get_all_labs(db:Session=Depends(get_db)):
    return lab_repo.show_all_labs(db)

@router.get("/{id}",response_model=schema.ShowLab,status_code=status.HTTP_200_OK)
def show_lab(id,db:Session=Depends(get_db)):
    return lab_repo.show(id,db)

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_lab(id,db:Session=Depends(get_db)):
    lab_repo.delete(id,db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# @router.get("/{lab_id}/experiments", status_code=status.HTTP_200_OK)
# def show_experiment_from_lab_id(lab_id, db: Session = Depends(get_db)):
#     return lab_repo.show_experiments_from_lab_id(lab_id, db)


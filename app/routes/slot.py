from fastapi import APIRouter, Depends,status,Response
from sqlalchemy.orm import Session
from app.config import database
from app.schema import schema
from app.repository import slot_repo


router=APIRouter(
    prefix="/slot",
    tags=['Slot']
)

get_db=database.get_db

@router.post("/",status_code=status.HTTP_201_CREATED)
def create_slot(request:schema.Slot,db:Session=Depends(get_db)):
    return slot_repo.create(request,db)

@router.get("/",status_code=status.HTTP_200_OK)
def get_all_slot(db:Session=Depends(get_db)):
    return slot_repo.show_all_slots(db)

@router.get("/{lab_id}",status_code=status.HTTP_200_OK)
def get_all_slots_from_lab_id(lab_id,db:Session=Depends(get_db)):
    return slot_repo.get_all_slots_from_lab_id(lab_id,db)


@router.get("/{id}",status_code=status.HTTP_200_OK)
def show_slot(id,db:Session=Depends(get_db)):
    return slot_repo.show(id,db)

@router.put("/{id}/{student_id}",status_code=status.HTTP_200_OK)
def show_slot(id,student_id,db:Session=Depends(get_db)):
    return slot_repo.updatebook(id,student_id,db)




@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_slot(id,db:Session=Depends(get_db)):
    slot_repo.delete(id,db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
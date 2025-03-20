from sqlalchemy.orm import Session
from . import crud, schemas

def register_user(db: Session, user_data: schemas.UserCreate):
    return crud.create_user(db, user_data)

def list_users(db: Session):
    return crud.get_users(db)

def fetch_user(db: Session, user_id: int):
    return crud.get_user(db, user_id)

def remove_user(db: Session, user_id: int):
    return crud.delete_user(db, user_id)

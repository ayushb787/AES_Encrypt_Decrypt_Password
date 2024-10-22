from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, models, database, security

router = APIRouter()

@router.post("/passwords/", response_model=schemas.PasswordResponse)
def create_password(password: schemas.PasswordCreate, db: Session = Depends(database.get_db)):
    db_password = crud.get_password_by_username(db, username=password.username)
    if db_password:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_password(db=db, password=password)

@router.get("/passwords/{username}")
def get_password(username: str, db: Session = Depends(database.get_db)):
    db_password = crud.get_password_by_username(db, username=username)
    if db_password is None:
        raise HTTPException(status_code=404, detail="Password not found")
    decrypted_password = security.decrypt_password(db_password.encrypted_password)
    return {"username": db_password.username, "service": db_password.service, "password": decrypted_password}

@router.get("/passwords/")
def get_all_passwords(db: Session = Depends(database.get_db)):
    return crud.get_all_passwords(db=db)

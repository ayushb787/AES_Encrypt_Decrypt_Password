from http.client import HTTPException

from sqlalchemy.orm import Session
import models
import schemas
import security


def create_password(db: Session, password: schemas.PasswordCreate):
    encrypted_password = security.encrypt_password(password.password)
    db_password = models.Password(
        username=password.username,
        service=password.service,
        encrypted_password=encrypted_password
    )
    db.add(db_password)
    db.commit()
    db.refresh(db_password)
    return db_password


def get_password_by_username(db: Session, username: str) -> models.Password:
    db_password = db.query(models.Password).filter(models.Password.username == username).first()

    if db_password is None:
        raise HTTPException(status_code=404, detail="Password not found for this username.")

    return db_password


def get_all_passwords(db: Session):
    return db.query(models.Password).all()

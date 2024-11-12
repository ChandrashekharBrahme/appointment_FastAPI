# app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas
from .auth import get_password_hash

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_booking(db: Session, booking: schemas.BookingCreate, user_id: int):
    db_booking = models.Booking(user_id=user_id, slot=booking.slot)
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

def get_all_bookings(db: Session):
    return db.query(models.Booking).all()

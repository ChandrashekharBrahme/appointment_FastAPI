# app/endpoints/user.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database, auth

router = APIRouter()

@router.post("/register/")
def register_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return crud.create_user(db=db, user=user)

@router.post("/book/")
def book_slot(booking: schemas.BookingCreate, db: Session = Depends(database.get_db), current_user: auth.User = Depends(auth.get_current_user)):
    return crud.create_booking(db=db, booking=booking, user_id=current_user.id)

# app/endpoints/admin.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, database, auth

router = APIRouter()

@router.get("/all-bookings/")
def read_all_bookings(db: Session = Depends(database.get_db), current_user: auth.User = Depends(auth.get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Not authorized")
    return crud.get_all_bookings(db)

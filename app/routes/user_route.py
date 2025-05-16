from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.controllers.user_controller import create_user
from app.db.session import get_db

router = APIRouter(prefix="/user")

@router.post("/create")
def register_user(data: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, data)

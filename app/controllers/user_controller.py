import uuid
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

def create_user(db: Session, data: UserCreate):
    session_id = str(uuid.uuid4())
    user = User(
        session=session_id,
        name=data.name,
        phone=data.phone,
        bb=data.bb,
        tb=data.tb,
        usia=data.usia,
        jenkel=data.jenkel
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"session": session_id}

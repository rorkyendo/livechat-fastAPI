from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base
import uuid

class User(Base):
    __tablename__ = "lv_chat_session"
    session = Column(
        String(36),
        primary_key=True,
        index=True,
        unique=True,
        default=lambda: str(uuid.uuid4())
    )
    name = Column(String(25), index=True)
    phone = Column(String(15), unique=True, index=True)
    bb = Column(Float, index=True)
    tb = Column(Float, index=True)
    usia = Column(Integer, index=True)
    jenkel = Column(String(1), index=True)

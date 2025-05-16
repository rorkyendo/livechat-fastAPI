from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    phone: str
    bb: float
    tb: float
    usia: int
    jenkel: str

from pydantic import BaseModel

class CarCreate(BaseModel):
    make: str
    model: str
    year: int
    price: float

class Car(CarCreate):
    id: int

    class Config:
        orm_mode = True

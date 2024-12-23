from sqlalchemy import Column, Integer, String, Float
from .database import Base

class CarModel(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True, index=True)
    make = Column(String, index=True)
    model = Column(String, index=True)
    year = Column(Integer)
    price = Column(Float)

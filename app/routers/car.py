from fastapi import APIRouter, Depends
from crouton import SQLAlchemyCRUDRouter
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db

router = APIRouter()

car_router = SQLAlchemyCRUDRouter(
    schema=schemas.Car,
    create_schema=schemas.CarCreate,
    db_model=models.CarModel,
    db=get_db,
    prefix="car"
)

router.include_router(car_router)

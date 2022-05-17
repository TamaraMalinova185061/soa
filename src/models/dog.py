from sqlalchemy import String, Boolean, Integer, Column
from src.enums import DogBreed, DogStatus
from sqlalchemy.dialects.postgresql import ENUM
from src.models.base import BaseDbModel, Base


class Dog(BaseDbModel, Base):
    name = Column(String(255), nullable=False)
    image_url = Column(String(255), nullable=True)
    is_chipped = Column(Boolean, default=False)
    coordinates = Column(String(255), nullable=True)
    breed = Column(ENUM(DogBreed, name="breeds"), name="breed", nullable=False)
    dog_status = Column(
        ENUM(DogStatus, name="statuses"), name="dog_status", nullable=False
    )

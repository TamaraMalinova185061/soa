from typing import Optional
from fastapi import APIRouter, Depends, Query

from src.schemas import ReadDogSchema, CreateDogSchema

from src.enums import DogStatus
from src.service.shelter import ShelterService, get_shelter_service


router = APIRouter(prefix="/shelter", tags=["Shelter"])


# @router.post("/adopt/{dog_id}", response_model=any)
# def adopt_dog(dog_id: str):
#     return ...
@router.get("/list_dogs_by_status")
async def list_dogs_by_status(
    status: Optional[DogStatus] = Query(None),
    shelter_service: ShelterService = Depends(get_shelter_service),
):
    return await shelter_service.list_dogs_by_status(status)


@router.post("/change_dog_status/{dog_id}", response_model=ReadDogSchema)
async def change_dog_status(
    dog_id: int,
    status: DogStatus,
    shelter_service: ShelterService = Depends(get_shelter_service),
):
    return await shelter_service.change_dog_status(dog_id, status)


@router.post("/place-dog-for-adoption", response_model=ReadDogSchema)
async def place_dog_for_adoption(
    dog: CreateDogSchema, shelter_service: ShelterService = Depends(get_shelter_service)
):
    return await shelter_service.create_dog(dog)


@router.get("/choose-next-dog-to-shelter", response_model=ReadDogSchema)
async def choose_next_dog_to_shelter(
    shelter_service: ShelterService = Depends(get_shelter_service),
):
    return await shelter_service.get_next_dog_to_shelter()

from typing import Optional
from fastapi import APIRouter, Depends, Query

from src.schemas import ReadDogSchema, CreateDogSchema

from src.enums import DogStatus
from src.service.shelter import ShelterService, get_shelter_service


router = APIRouter(prefix="/shelter", tags=["Shelter"])


@router.get("/report-found-dog", response_model=ReadDogSchema)
async def report_found_dog(

):
    return await None

from fastapi import APIRouter
from src.api import shelter


router = APIRouter(prefix="/api/v1")
router.include_router(shelter.router)

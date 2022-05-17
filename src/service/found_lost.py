from src.enums import LostDogReportStatus
from src.repository.found_lost import FoundLostRepository, get_found_lost_repository
from typing import List, Optional
from fastapi import Depends, HTTPException, status
from pydantic import EmailStr
from src import integration
from src.database import ScopedSession
from sqlalchemy.exc import DatabaseError

from src.schemas import ReadLostDogReportSchema

class FoundLostService:
    def __init__(self, found_lost_repository: FoundLostRepository):
        self.repository = found_lost_repository

    async def change_report_status(
            self, found_dog_report_id: str, report_status: LostDogReportStatus
    ) -> ReadLostDogReportSchema:
        try:
            async with ScopedSession() as active_session:
                async with active_session.begin():
                    dog = await self.repository.change_report_status(
                        found_dog_report_id, report_status, session=active_session
                    )
                    return self._return_schema.from_orm(dog)
        except DatabaseError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="There was an error changing report status",
            )




def get_found_lost_service(
        found_lost_repository: FoundLostRepository = Depends(get_found_lost_repository),
):
    return FoundLostService(found_lost_repository=found_lost_repository)

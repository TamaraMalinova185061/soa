from src.enums import LostDogReportStatus
from src.repository.lost_found import LostFoundRepository, get_lost_found_repository
from typing import List, Optional
from fastapi import Depends, HTTPException, status
from pydantic import EmailStr
from src import integration
from src.database import ScopedSession
from sqlalchemy.exc import DatabaseError

from src.schemas import ReadLostDogReportSchema

class LostFoundService:
    def __init__(self, lost_found_repository: LostFoundRepository):
        self.repository = lost_found_repository

    async def change_report_status(
            self, lost_dog_report_id: str, report_status: LostDogReportStatus
    ) -> ReadLostDogReportSchema:
        try:
            async with ScopedSession() as active_session:
                async with active_session.begin():
                    dog = await self.repository.change_report_status(
                        lost_dog_report_id, report_status, session=active_session
                    )
                    return self._return_schema.from_orm(dog)
        except DatabaseError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="There was an error changing report status",
            )




def get_lost_found_service(
        lost_found_repository: LostFoundRepository = Depends(get_lost_found_repository),
):
    return LostFoundService(lost_found_repository=lost_found_repository)

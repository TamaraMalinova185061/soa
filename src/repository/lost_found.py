from typing import List, Optional
from sqlalchemy import asc
from sqlalchemy.orm import scoped_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import select, update

from src.models.lost_dog_report import LostDogReport
from src.enums import LostDogReportStatus

class LostFoundRepository:
    async def find_one(self, id_: int, session: AsyncSession) -> Optional[LostDogReport]:
        statement = select(LostDogReport).where(LostDogReport.id_ == id_)
        result = await session.execute(statement)
        return result.scalars().first()

    async def change_report_status(
        self, lost_dog_report_id: str, report_status: LostDogReportStatus, session: AsyncSession
    ) -> LostDogReport:
        statement = update(LostDogReport).values(report_status=report_status).where(LostDogReport.id_ == lost_dog_report_id)
        await session.execute(statement)
        return await self.find_one(lost_dog_report_id, session)

    async def list_reports_by_status(
        self, report_status: LostDogReportStatus, session: AsyncSession
    ) -> List[LostDogReport]:
        statement = select(LostDogReport).where(LostDogReport.report_status == report_status)
        result = await session.execute(statement)
        return result.unique().scalars().all()

    async def insert_one(self, report: LostDogReport, session: AsyncSession) -> LostDogReport:
        session.add(report)
        await session.flush()
        await session.refresh(report)
        return report

    # async def find_next_to_shelter(self, session: AsyncSession) -> Dog:
    #     statement = (
    #         select(Dog)
    #         .where(Dog.dog_status == DogStatus.WAITING)
    #         .order_by(asc(Dog.created_at))
    #         .limit(1)
    #     )
    #     result = await session.execute(statement)
    #     return result.scalars().first()


def get_lost_found_repository():
    return LostFoundRepository
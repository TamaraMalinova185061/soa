from typing import List, Optional
from sqlalchemy import asc
from sqlalchemy.orm import scoped_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import select, update

from src.models.found_dog_report import FoundDogReport
from src.enums import LostDogReportStatus

class FoundLostRepository:
    async def find_one(self, id_: int, session: AsyncSession) -> Optional[FoundDogReport]:
        statement = select(FoundDogReport).where(FoundDogReport.id_ == id_)
        result = await session.execute(statement)
        return result.scalars().first()

    async def change_report_status(
        self, found_dog_report_id: str, report_status: LostDogReportStatus, session: AsyncSession
    ) -> FoundDogReport:
        statement = update(FoundDogReport).values(report_status=report_status).where(FoundDogReport.id_ == found_dog_report_id)
        await session.execute(statement)
        return await self.find_one(found_dog_report_id, session)

    async def list_reports_by_status(
        self, report_status: LostDogReportStatus, session: AsyncSession
    ) -> List[FoundDogReport]:
        statement = select(FoundDogReport).where(FoundDogReport.report_status == report_status)
        result = await session.execute(statement)
        return result.unique().scalars().all()

    async def insert_one(self, report: FoundDogReport, session: AsyncSession) -> FoundDogReport:
        session.add(report)
        await session.flush()
        await session.refresh(report)
        return report



def get_found_lost_repository():
    return FoundLostRepository
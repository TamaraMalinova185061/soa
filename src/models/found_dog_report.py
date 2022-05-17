from sqlalchemy import String, Boolean, Integer, Column
from sqlalchemy.dialects.postgresql import ENUM
from src.models.base import BaseDbModel, Base
from ..enums import FoundDogReportStatus


class FoundDogReport(BaseDbModel, Base):
    __tablename__ = "lost_dog_reports"
    id = Column(Integer, primary_key=True)
    image_url = Column(String(255), nullable=True)
    user_name = Column(String(255), nullable=False)
    phone_number = Column(String(255), nullable=False)
    dog_name = Column(String(255), nullable=False)
    is_chipped = Column(Boolean, default=False)
    last_known_location = Column(String(255), nullable=True)
    report_status = Column(
        ENUM(FoundDogReportStatus, name="statuses"),
        name="report_status",
        nullable=False
    )

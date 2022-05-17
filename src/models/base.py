from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import declarative_mixin, declared_attr, declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


@declarative_mixin
class BaseDbModel:
    id_ = Column("id", Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

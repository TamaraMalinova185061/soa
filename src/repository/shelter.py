from typing import List, Optional
from sqlalchemy import asc
from sqlalchemy.orm import scoped_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import select, update

from src.models.dog import Dog
from src.enums import DogStatus


class ShelterRepository:
    async def find_one(self, id_: int, session: AsyncSession) -> Optional[Dog]:
        statement = select(Dog).where(Dog.id_ == id_)
        result = await session.execute(statement)
        return result.scalars().first()

    async def change_dog_status(
        self, dog_id: str, dog_status: DogStatus, session: AsyncSession
    ) -> Dog:
        statement = update(Dog).values(dog_status=dog_status).where(Dog.id_ == dog_id)
        await session.execute(statement)
        return await self.find_one(dog_id, session)

    async def list_dogs_by_status(
        self, dog_status: DogStatus, session: AsyncSession
    ) -> List[Dog]:
        statement = select(Dog).where(Dog.dog_status == dog_status)
        result = await session.execute(statement)
        return result.unique().scalars().all()

    async def insert_one(self, dog: Dog, session: AsyncSession) -> Dog:
        session.add(dog)
        await session.flush()
        await session.refresh(dog)
        return dog

    async def find_next_to_shelter(self, session: AsyncSession) -> Dog:
        statement = (
            select(Dog)
            .where(Dog.dog_status == DogStatus.WAITING)
            .order_by(asc(Dog.created_at))
            .limit(1)
        )
        result = await session.execute(statement)
        return result.scalars().first()


def get_shelter_repository():
    return ShelterRepository()

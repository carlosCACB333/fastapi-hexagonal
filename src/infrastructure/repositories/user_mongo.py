""" User repository implementation using SQLAlchemy """

import logging
from typing import List

from motor.motor_asyncio import AsyncIOMotorDatabase

from src.domain.model.user import UserModel
from src.domain.repositories.user import UserMongoRepositoryInterface

logger = logging.getLogger(__name__)


class UserMongoRepository(UserMongoRepositoryInterface):
    """User repository implementation using SQLAlchemy"""

    def __init__(self, session: AsyncIOMotorDatabase):
        self.collection = session.get_collection("users")

    async def create(self, user: UserModel) -> UserModel:

        user = {
            "id": user.id,
            "email": user.email,
            "password": user.password,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "created_at": user.created_at,
            "updated_at": user.updated_at,
        }
        await self.collection.insert_one(user)
        return UserModel(
            id=user["id"],
            email=user["email"],
            password=user["password"],
            first_name=user["first_name"],
            last_name=user["last_name"],
            created_at=user["created_at"],
            updated_at=user["updated_at"],
        )

    async def find_all(self) -> List[UserModel]:
        users = await self.collection.find().to_list(length=None)
        users = [
            UserModel(
                id=user["id"],
                email=user["email"],
                password=user["password"],
                first_name=user["first_name"],
                last_name=user["last_name"],
                created_at=user["created_at"],
                updated_at=user["updated_at"],
            )
            for user in users
        ]

        return users

    async def find_by_id(self, user_id: int) -> UserModel | None:
        user = await self.collection.find_one({"id": user_id})
        if not user:
            return None
        return UserModel(
            id=user["id"],
            email=user["email"],
            password=user["password"],
            first_name=user["first_name"],
            last_name=user["last_name"],
            created_at=user["created_at"],
            updated_at=user["updated_at"],
        )

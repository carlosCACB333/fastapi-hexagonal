""" User Repository Interface """

from abc import ABC, abstractmethod
from typing import List, Union

from src.domain.model.user import UserModel


class UserPgRepositoryInterface(ABC):
    """User Repository Interface"""

    @abstractmethod
    def create(self, user: UserModel) -> UserModel:
        """Create a user."""
        raise NotImplementedError


class UserMongoRepositoryInterface(ABC):
    """User Query Repository Interface"""

    @abstractmethod
    async def create(self, user: UserModel) -> UserModel:
        """Create a user."""
        raise NotImplementedError

    @abstractmethod
    async def find_all(self) -> List[UserModel]:
        """Find all users."""
        raise NotImplementedError

    @abstractmethod
    async def find_by_id(self, user_id: int) -> Union[UserModel, None]:
        """Find a user by ID."""
        raise NotImplementedError

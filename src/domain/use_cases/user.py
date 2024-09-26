""" User use cases module """

from abc import ABC, abstractmethod
from typing import List

from src.domain.model.user import UserModel
from src.domain.repositories.user import (
    UserMongoRepositoryInterface,
    UserPgRepositoryInterface,
)


class UserCommandUseCases(ABC):
    """User use cases class."""

    def __init__(
        self,
        user_repository: UserPgRepositoryInterface,
    ):
        self.user_repository = user_repository

    @abstractmethod
    def create(self, user: UserModel) -> UserModel:
        """Create a user."""
        raise NotImplementedError


class UserQueryUseCases(ABC):
    """User use cases class."""

    def __init__(
        self,
        user_repository: UserMongoRepositoryInterface,
    ):
        self.user_repository = user_repository

    @abstractmethod
    def create(self, user: UserModel) -> UserModel:
        """Create a user."""
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> List[UserModel]:
        """Find all users."""
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, user_id: int) -> UserModel:
        """Find a user by ID."""
        raise NotImplementedError

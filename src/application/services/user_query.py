"""User service module."""

import logging

from src.domain.exceptions.user import UserNotFound
from src.domain.model.user import UserModel
from src.domain.use_cases.user import UserQueryUseCases

logger = logging.getLogger(__name__)


class UserQueryService(UserQueryUseCases):
    """User service class."""

    def create(self, user: UserModel):
        return self.user_repository.create(user)

    def find_all(self):
        return self.user_repository.find_all()

    def find_by_id(self, user_id: int) -> UserModel:
        user = self.user_repository.find_by_id(user_id)
        if not user:
            raise UserNotFound()
        return user

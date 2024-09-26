"""User service module."""

from sqlalchemy.exc import IntegrityError

from src.application.validators.user import UserValidator
from src.domain.exceptions.user import UserEmailAlreadyExists
from src.domain.model.user import UserModel
from src.domain.use_cases.user import UserCommandUseCases


class UserCommandService(UserCommandUseCases):
    """User service class."""

    def create(self, user: UserModel):
        UserValidator.validate_email(user.email)
        try:
            user = self.user_repository.create(user)
            return user
        except IntegrityError as e:
            raise UserEmailAlreadyExists() from e

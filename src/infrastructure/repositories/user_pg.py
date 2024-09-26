""" User repository implementation using SQLAlchemy """

from sqlalchemy.orm import Session

from src.domain.model.user import UserModel
from src.domain.repositories.user import UserPgRepositoryInterface
from src.infrastructure.entities.user import User


class UserPgRepository(UserPgRepositoryInterface):
    """User repository implementation using SQLAlchemy"""

    def __init__(self, session: Session):
        self.session = session

    def create(self, user: UserModel) -> UserModel:
        new_user = User(
            email=user.email,
            password=user.password,
            first_name=user.first_name,
            last_name=user.last_name,
        )
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)

        return UserModel(**new_user.dict())

"""User schemas module."""

from datetime import datetime

from pydantic import BaseModel, Field

from src.infrastructure.schemas.base import BaseRequest, BaseResponse


class CreateUserReq(BaseRequest):
    """Create user request model."""

    email: str = Field(
        "jhon@gmail.com",
        pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
    )

    first_name: str = Field(
        "John",
    )

    last_name: str = Field(
        "Doe",
    )

    password: str = Field(
        "1234",
        title="User password",
        min_length=4,
        max_length=8,
    )


class User(BaseModel):
    """Data model."""

    id: int
    email: str
    password: str
    first_name: str
    last_name: str
    created_at: datetime
    updated_at: datetime


class CreateUserRes(BaseResponse):
    """Create user response model."""

    data: User


class GetUserRes(BaseResponse):
    """Get user response model."""

    data: User


class GetUsersRes(BaseResponse):
    """Get users response model."""

    data: list[User]

""" User exceptions """

from src.domain.exceptions.base import AppError


class InvalidEmail(AppError):
    """Invalid email exception."""

    def __init__(self):
        super().__init__("Invalid email value")


class UserNotFound(AppError):
    """User not found exception."""

    def __init__(self):
        super().__init__("User not found", status_code=404)


class UserEmailAlreadyExists(AppError):
    """User email already exists exception."""

    def __init__(self):
        super().__init__("User email already exists")

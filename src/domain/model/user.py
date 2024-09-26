"""User entity module."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class UserModel:
    """User entity class."""

    id: Optional[int] = None
    email: Optional[str] = None
    password: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def dict(self):
        """Convert to dictionary."""
        return self.__dict__

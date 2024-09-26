"""User validators"""

import re

from src.domain.exceptions.user import InvalidEmail


class UserValidator:
    """User validators"""

    @staticmethod
    def validate_email(email: str):
        """Validate email with regex: (^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"""
        if not re.match(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
            email,
        ):
            raise InvalidEmail()

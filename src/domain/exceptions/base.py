""" Base exception class for the application """

from typing import Union

from src.infrastructure.config.constants import ResponseStatus


class AppError(Exception):
    """Base exception class for the application"""

    def __init__(
        self,
        message: str,
        status_code: int = 500,
        code_error: str = "00",
        data: Union[dict, list] = None,
    ):
        super().__init__(message)
        self.status = ResponseStatus.FAILED
        self.status_code = status_code
        self.code_error = code_error
        self.message = message
        self.data = data

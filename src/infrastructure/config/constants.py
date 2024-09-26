""" Constants for the application """

from enum import Enum


class ResponseStatus(str, Enum):
    """Response status constants"""

    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"

"""Base schemas module"""

from typing import Optional

from pydantic import BaseModel, Field

from src.infrastructure.config.constants import ResponseStatus


class BaseRequest(BaseModel):
    """Base request model"""


class BaseResponse(BaseModel):
    """Base response model"""

    status: ResponseStatus = ResponseStatus.SUCCEEDED
    message: str = ""


class ErrorResponse(BaseResponse):
    """Error response model"""

    status_code: int = Field(500, title="HTTP status code")
    status: ResponseStatus = Field(ResponseStatus.FAILED, title="Response status")
    code_error: str = Field("00", title="Error code")
    message: str = Field("Internal Server Error", title="Error message")
    data: Optional[dict[str, str]] = Field(None, title="Error data")

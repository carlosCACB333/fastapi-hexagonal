"""Entry point of the application."""

import logging
import time
import traceback
from contextlib import asynccontextmanager

from fastapi import APIRouter, FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from src.domain.exceptions.base import AppError
from src.infrastructure.config.database import Base, engine
from src.infrastructure.config.settings import Settings
from src.infrastructure.handlers import Handlers
from src.infrastructure.schemas.base import ErrorResponse

logging.basicConfig(format=Settings.LOG_FORMAT, level=Settings.LOG_LEVEL)
logger = logging.getLogger(__name__)
for logger_name in logging.Logger.manager.loggerDict:
    logger = logging.getLogger(logger_name)
    for handler in logger.handlers:
        handler.setFormatter(logging.Formatter(Settings.LOG_FORMAT))


@asynccontextmanager
async def lifespan(_app: FastAPI):
    """Context manager to handle the application lifespan."""
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title=Settings.PROJECT_NAME,
    description=Settings.PROJECT_DESCRIPTION,
    version=Settings.PROJECT_VERSION,
    debug=Settings.DEBUG,
    lifespan=lifespan,
)


router = APIRouter(
    prefix=Settings.API_PREFIX,
    responses={
        422: {
            "description": "Validation Error",
            "model": ErrorResponse,
        },
        500: {
            "description": "Internal Server Error",
            "model": ErrorResponse,
        },
    },
)

for handler in Handlers.iterator():
    router.include_router(handler.router)

app.include_router(router)


@app.exception_handler(AppError)
async def base_exception_handler(_: Request, exc: AppError):
    """Handle application exceptions."""
    logger.error(exc)
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.__dict__,
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_: Request, exc: RequestValidationError):
    """Handle validation exceptions."""
    logger.error(exc)
    errors = {}
    for e in exc.errors():
        field = e["loc"][-1]
        message = e["msg"]
        errors[field] = message

    return JSONResponse(
        status_code=422,
        content=ErrorResponse(
            status_code=422,
            data=errors,
            message="Validation Error",
        ).model_dump(),
    )


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """Middleware to add process time header."""
    start_time = time.perf_counter()
    try:
        response = await call_next(request)
    except Exception:
        logger.error(traceback.format_exc())
        response = JSONResponse(
            status_code=500,
            content=ErrorResponse().dict(),
        )
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

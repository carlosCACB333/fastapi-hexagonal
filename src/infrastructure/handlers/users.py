"""User handlers."""

import logging

from fastapi import APIRouter, BackgroundTasks, Depends
from sqlalchemy.orm import Session

from src.application.services.user_command import UserCommandService
from src.application.services.user_query import UserQueryService
from src.domain.model.user import UserModel
from src.infrastructure.config.database import get_pg_db, mongo_client
from src.infrastructure.repositories.user_mongo import UserMongoRepository
from src.infrastructure.repositories.user_pg import UserPgRepository
from src.infrastructure.schemas.user import (
    CreateUserReq,
    CreateUserRes,
    GetUserRes,
    GetUsersRes,
)

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("/", response_model=CreateUserRes)
async def create_user(
    background_tasks: BackgroundTasks,
    user_req: CreateUserReq,
    db: Session = Depends(get_pg_db),
):
    """Create a new user."""

    service = UserCommandService(UserPgRepository(db))

    user = service.create(UserModel(**user_req.model_dump()))
    mongo_service = UserQueryService(UserMongoRepository(mongo_client))

    async def create_user_mongo(user: UserModel):
        await mongo_service.create(user)

    background_tasks.add_task(create_user_mongo, user)

    return CreateUserRes(data=user.dict())


@router.get("/", response_model=GetUsersRes)
async def get_users():
    """Get all users."""
    service = UserQueryService(UserMongoRepository(mongo_client))
    users = await service.find_all()
    return GetUsersRes(data=[user.dict() for user in users])


@router.get("/{user_id}", response_model=GetUserRes)
async def get_user(user_id: int):
    """Get user by id."""
    service = UserQueryService(UserMongoRepository(mongo_client))
    user = await service.find_by_id(user_id)
    return GetUserRes(data=user.dict())

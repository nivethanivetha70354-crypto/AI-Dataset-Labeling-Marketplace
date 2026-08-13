from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService
from app.utils.security import hash_password


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post(
    "/",
    response_model=UserResponse,
    status_code=201,
)
def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db),
):
    service = UserService(db)

    try:
        user = service.create_user(
            name=user_data.name,
            email=user_data.email,
            password=hash_password(user_data.password),
            role=user_data.role,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )

    return user


@router.get(
    "/",
    response_model=list[UserResponse],
)
def get_users(
    db: Session = Depends(get_db),
):
    service = UserService(db)

    return service.get_all_users()


@router.get(
    "/{user_id}",
    response_model=UserResponse,
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    service = UserService(db)

    user = service.get_user_by_id(user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return user
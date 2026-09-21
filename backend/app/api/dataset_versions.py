from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.auth import require_client, get_current_user
from app.database.connection import get_db
from app.models.dataset import Dataset
from app.models.dataset_version import DatasetVersion
from app.models.user import User
from app.schemas.dataset_version import (
    DatasetVersionCreate,
    DatasetVersionResponse,
)

router = APIRouter(
    prefix="/dataset-versions",
    tags=["Dataset Versions"],
)


@router.post(
    "/",
    response_model=DatasetVersionResponse,
    status_code=201,
)
def create_dataset_version(
    data: DatasetVersionCreate,
    current_user: User = Depends(require_client),
    db: Session = Depends(get_db),
):
    dataset = db.get(Dataset, data.dataset_id)

    if dataset is None:
        raise HTTPException(
            status_code=404,
            detail="Dataset not found",
        )

    if dataset.owner_id != current_user.user_id:
        raise HTTPException(
            status_code=403,
            detail="You can only create versions for your own dataset",
        )

    existing_version = db.execute(
        select(DatasetVersion).where(
            DatasetVersion.dataset_id == data.dataset_id,
            DatasetVersion.version_number == data.version_number,
        )
    ).scalar_one_or_none()

    if existing_version is not None:
        raise HTTPException(
            status_code=400,
            detail="This version already exists",
        )

    version = DatasetVersion(
        dataset_id=data.dataset_id,
        version_number=data.version_number,
        description=data.description,
        status="created",
    )

    db.add(version)
    db.commit()
    db.refresh(version)

    return version


@router.get(
    "/",
    response_model=list[DatasetVersionResponse],
)
def get_dataset_versions(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    result = db.execute(
        select(DatasetVersion)
    )

    return result.scalars().all()


@router.get(
    "/{version_id}",
    response_model=DatasetVersionResponse,
)
def get_dataset_version(
    version_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    version = db.get(DatasetVersion, version_id)

    if version is None:
        raise HTTPException(
            status_code=404,
            detail="Dataset version not found",
        )

    return version
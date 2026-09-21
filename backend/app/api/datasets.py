import os
import shutil

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.auth import require_client, get_current_user
from app.database.connection import get_db
from app.models.dataset import Dataset
from app.models.user import User
from app.schemas.dataset import DatasetResponse

router = APIRouter(prefix="/datasets", tags=["Datasets"])

UPLOAD_DIR = "uploads/datasets"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.get("/", response_model=list[DatasetResponse])
def get_datasets(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.role == "client":
        result = db.execute(
            select(Dataset).where(
                Dataset.owner_id == current_user.user_id
            )
        )
    else:
        result = db.execute(select(Dataset))

    return result.scalars().all()
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.dataset import Dataset
from app.schemas.dataset import DatasetCreate, DatasetResponse

router = APIRouter(prefix="/datasets", tags=["Datasets"])


@router.post("/", response_model=DatasetResponse, status_code=201)
def create_dataset(
    dataset_data: DatasetCreate,
    db: Session = Depends(get_db),
):
    dataset = Dataset(
        name=dataset_data.name,
        description=dataset_data.description,
        file_path=dataset_data.file_path,
    )

    db.add(dataset)
    db.commit()
    db.refresh(dataset)

    return dataset


@router.get("/", response_model=list[DatasetResponse])
def get_datasets(db: Session = Depends(get_db)):
    result = db.execute(select(Dataset))
    return result.scalars().all()


@router.get("/{dataset_id}", response_model=DatasetResponse)
def get_dataset(dataset_id: int, db: Session = Depends(get_db)):
    dataset = db.get(Dataset, dataset_id)

    if dataset is None:
        raise HTTPException(
            status_code=404,
            detail="Dataset not found",
        )

    return dataset
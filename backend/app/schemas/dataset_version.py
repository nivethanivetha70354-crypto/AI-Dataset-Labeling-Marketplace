from datetime import datetime

from pydantic import BaseModel, ConfigDict


class DatasetVersionCreate(BaseModel):
    dataset_id: int
    version_number: int
    description: str | None = None


class DatasetVersionResponse(BaseModel):
    version_id: int
    dataset_id: int
    version_number: int
    description: str | None
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
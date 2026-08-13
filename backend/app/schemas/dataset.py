from pydantic import BaseModel


class DatasetCreate(BaseModel):
    name: str
    description: str | None = None
    file_path: str | None = None


class DatasetResponse(BaseModel):
    dataset_id: int
    name: str
    description: str | None
    file_path: str | None
    status: str

    model_config = {
        "from_attributes": True
    }
from pydantic import BaseModel


class TaskCreate(BaseModel):
    dataset_id: int
    title: str
    instructions: str | None = None


class TaskResponse(BaseModel):
    task_id: int
    dataset_id: int
    title: str
    instructions: str | None
    status: str

    model_config = {
        "from_attributes": True
    }
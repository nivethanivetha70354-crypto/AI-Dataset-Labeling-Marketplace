from datetime import datetime

from pydantic import BaseModel, ConfigDict


class SubmissionCreate(BaseModel):
    task_id: int
    labels: str


class SubmissionResponse(BaseModel):
    submission_id: int
    task_id: int
    annotator_id: int
    labels: str
    status: str
    submitted_at: datetime

    model_config = ConfigDict(from_attributes=True)
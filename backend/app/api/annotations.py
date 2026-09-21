from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.api.auth import require_annotator, get_current_user
from app.database.connection import get_db
from app.models.annotation import Annotation
from app.models.task import Task
from app.models.task_assignment import TaskAssignment
from app.models.user import User

router = APIRouter(
    prefix="/annotations",
    tags=["Annotations"],
)


class AnnotationCreate(BaseModel):
    task_id: int
    input_text: str
    ai_label: str
    final_label: str
    confidence: float


@router.post("/", status_code=201)
def create_annotation(
    data: AnnotationCreate,
    current_user: User = Depends(require_annotator),
    db: Session = Depends(get_db),
):
    task = db.get(Task, data.task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    assignment = (
        db.query(TaskAssignment)
        .filter(
            TaskAssignment.task_id == data.task_id,
            TaskAssignment.annotator_id == current_user.user_id,
            TaskAssignment.status == "accepted",
        )
        .first()
    )

    if assignment is None:
        raise HTTPException(
            status_code=403,
            detail="You must accept the task first",
        )

    annotation = Annotation(
        task_id=data.task_id,
        annotator_id=current_user.user_id,
        input_text=data.input_text,
        ai_label=data.ai_label,
        final_label=data.final_label,
        confidence=data.confidence,
        status="verified",
    )

    db.add(annotation)
    db.commit()
    db.refresh(annotation)

    return {
        "success": True,
        "data": {
            "annotation_id": annotation.annotation_id,
            "task_id": annotation.task_id,
            "annotator_id": annotation.annotator_id,
            "input_text": annotation.input_text,
            "ai_label": annotation.ai_label,
            "final_label": annotation.final_label,
            "confidence": annotation.confidence,
            "status": annotation.status,
        },
        "message": "Annotation saved successfully",
    }


@router.get("/")
def get_annotations(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    annotations = db.query(Annotation).all()

    return {
        "success": True,
        "data": annotations,
        "message": "Annotations retrieved successfully",
    }
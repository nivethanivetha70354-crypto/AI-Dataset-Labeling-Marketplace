from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.auth import get_current_user, require_annotator, require_client
from app.database.connection import get_db
from app.models.task import Task
from app.models.task_assignment import TaskAssignment
from app.models.user import User
from app.schemas.submission import SubmissionCreate, SubmissionResponse
from app.services.submission_service import SubmissionService

router = APIRouter(prefix="/submissions", tags=["Submissions"])


@router.post("/", response_model=SubmissionResponse, status_code=201)
def create_submission(
    submission_data: SubmissionCreate,
    current_user: User = Depends(require_annotator),
    db: Session = Depends(get_db),
):
    task = db.get(Task, submission_data.task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    assignment = (
        db.query(TaskAssignment)
        .filter(
            TaskAssignment.task_id == submission_data.task_id,
            TaskAssignment.annotator_id == current_user.user_id,
            TaskAssignment.status == "accepted",
        )
        .first()
    )

    if assignment is None:
        raise HTTPException(
            status_code=403,
            detail="You must accept the task before submitting",
        )

    service = SubmissionService(db)

    return service.create_submission(
        task_id=submission_data.task_id,
        annotator_id=current_user.user_id,
        labels=submission_data.labels,
    )


@router.get("/", response_model=list[SubmissionResponse])
def get_submissions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = SubmissionService(db)
    return service.get_all_submissions()


@router.get("/{submission_id}", response_model=SubmissionResponse)
def get_submission(
    submission_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = SubmissionService(db)

    submission = service.get_submission_by_id(submission_id)

    if submission is None:
        raise HTTPException(
            status_code=404,
            detail="Submission not found",
        )

    return submission


@router.put("/{submission_id}/approve", response_model=SubmissionResponse)
def approve_submission(
    submission_id: int,
    current_user: User = Depends(require_client),
    db: Session = Depends(get_db),
):
    service = SubmissionService(db)

    submission = service.get_submission_by_id(submission_id)

    if submission is None:
        raise HTTPException(
            status_code=404,
            detail="Submission not found",
        )

    submission.status = "approved"

    task = db.get(Task, submission.task_id)

    if task is not None:
        task.status = "completed"

    db.commit()
    db.refresh(submission)

    return submission


@router.put("/{submission_id}/reject", response_model=SubmissionResponse)
def reject_submission(
    submission_id: int,
    current_user: User = Depends(require_client),
    db: Session = Depends(get_db),
):
    service = SubmissionService(db)

    submission = service.get_submission_by_id(submission_id)

    if submission is None:
        raise HTTPException(
            status_code=404,
            detail="Submission not found",
        )

    submission.status = "rejected"

    db.commit()
    db.refresh(submission)

    return submission
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.auth import require_annotator
from app.database.connection import get_db
from app.models.task import Task
from app.models.task_assignment import TaskAssignment
from app.models.user import User

router = APIRouter(
    prefix="/assignments",
    tags=["Task Assignments"],
)


@router.post("/{task_id}", status_code=201)
def accept_task(
    task_id: int,
    current_user: User = Depends(require_annotator),
    db: Session = Depends(get_db),
):
    task = db.get(Task, task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    if task.status != "open":
        raise HTTPException(
            status_code=400,
            detail="Task is not open",
        )

    existing_assignment = (
        db.query(TaskAssignment)
        .filter(
            TaskAssignment.task_id == task_id,
            TaskAssignment.annotator_id == current_user.user_id,
        )
        .first()
    )

    if existing_assignment:
        raise HTTPException(
            status_code=400,
            detail="You already accepted this task",
        )

    assignment = TaskAssignment(
        task_id=task_id,
        annotator_id=current_user.user_id,
        status="accepted",
    )

    db.add(assignment)
    db.commit()
    db.refresh(assignment)

    return {
        "assignment_id": assignment.assignment_id,
        "task_id": assignment.task_id,
        "annotator_id": assignment.annotator_id,
        "status": assignment.status,
        "message": "Task accepted successfully",
    }


@router.get("/")
def get_my_assignments(
    current_user: User = Depends(require_annotator),
    db: Session = Depends(get_db),
):
    assignments = (
        db.query(TaskAssignment)
        .filter(
            TaskAssignment.annotator_id == current_user.user_id
        )
        .all()
    )

    return [
        {
            "assignment_id": assignment.assignment_id,
            "task_id": assignment.task_id,
            "annotator_id": assignment.annotator_id,
            "status": assignment.status,
            "assigned_at": assignment.assigned_at,
        }
        for assignment in assignments
    ]
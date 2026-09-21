from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.auth import require_client, get_current_user
from app.database.connection import get_db
from app.models.dataset import Dataset
from app.models.task import Task
from app.models.user import User
from app.schemas.task import TaskCreate, TaskResponse

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)


@router.post(
    "/",
    response_model=TaskResponse,
    status_code=201,
)
def create_task(
    task_data: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_client),
):
    dataset = db.get(Dataset, task_data.dataset_id)

    if dataset is None:
        raise HTTPException(
            status_code=404,
            detail="Dataset not found",
        )

    if dataset.owner_id != current_user.user_id:
        raise HTTPException(
            status_code=403,
            detail="You can only create tasks for your own datasets",
        )

    task = Task(
        dataset_id=task_data.dataset_id,
        owner_id=current_user.user_id,
        title=task_data.title,
        instructions=task_data.instructions,
        status="open",
        progress=0,
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


@router.get(
    "/",
    response_model=list[TaskResponse],
)
def get_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = db.execute(select(Task))
    return result.scalars().all()


@router.get(
    "/{task_id}",
    response_model=TaskResponse,
)
def get_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = db.get(Task, task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    return task


@router.put("/{task_id}/progress")
def update_task_progress(
    task_id: int,
    progress: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_client),
):
    task = db.get(Task, task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    if task.owner_id != current_user.user_id:
        raise HTTPException(
            status_code=403,
            detail="You can only update your own task",
        )

    if progress < 0 or progress > 100:
        raise HTTPException(
            status_code=400,
            detail="Progress must be between 0 and 100",
        )

    task.progress = progress

    if progress == 100:
        task.status = "completed"
    elif progress > 0:
        task.status = "in_progress"
    else:
        task.status = "open"

    db.commit()
    db.refresh(task)

    return {
        "success": True,
        "data": {
            "task_id": task.task_id,
            "progress": task.progress,
            "status": task.status,
        },
        "message": "Task progress updated successfully",
    }
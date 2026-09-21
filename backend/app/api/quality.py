from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.auth import get_current_user
from app.database.connection import get_db
from app.models.annotation import Annotation
from app.models.user import User
from app.services.quality_service import calculate_quality

router = APIRouter(
    prefix="/quality",
    tags=["Quality Measurement"],
)


@router.get("/{annotation_id}")
def get_annotation_quality(
    annotation_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    annotation = db.get(Annotation, annotation_id)

    if annotation is None:
        raise HTTPException(
            status_code=404,
            detail="Annotation not found",
        )

    score = calculate_quality(
        annotation.ai_label,
        annotation.final_label,
    )

    return {
        "success": True,
        "data": {
            "annotation_id": annotation.annotation_id,
            "ai_label": annotation.ai_label,
            "final_label": annotation.final_label,
            "quality_score": score,
        },
        "message": "Quality score calculated successfully",
    }
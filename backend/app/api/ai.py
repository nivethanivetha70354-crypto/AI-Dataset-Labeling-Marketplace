from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.api.auth import require_annotator
from app.models.user import User
from app.services.ai_label_service import generate_label_suggestion

router = APIRouter(
    prefix="/ai",
    tags=["AI Assistance"],
)


class LabelSuggestionRequest(BaseModel):
    text: str


@router.post("/suggest-label")
def suggest_label(
    data: LabelSuggestionRequest,
    current_user: User = Depends(require_annotator),
):
    result = generate_label_suggestion(data.text)

    return {
        "success": True,
        "data": result,
        "message": "AI label suggestion generated successfully",
    }
from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text

from app.database.connection import Base


class Submission(Base):
    __tablename__ = "submissions"

    submission_id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.task_id"), nullable=False)
    annotator_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    labels = Column(Text, nullable=False)
    status = Column(String, default="submitted")
    submitted_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
    )
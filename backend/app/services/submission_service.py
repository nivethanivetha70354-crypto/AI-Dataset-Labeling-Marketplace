from sqlalchemy.orm import Session

from app.models.submission import Submission


class SubmissionService:

    def __init__(self, db: Session):
        self.db = db

    def create_submission(
        self,
        task_id: int,
        annotator_id: int,
        labels: str,
    ):
        submission = Submission(
            task_id=task_id,
            annotator_id=annotator_id,
            labels=labels,
            status="submitted",
        )

        self.db.add(submission)
        self.db.commit()
        self.db.refresh(submission)

        return submission

    def get_all_submissions(self):
        return self.db.query(Submission).all()

    def get_submission_by_id(self, submission_id: int):
        return self.db.get(Submission, submission_id)

    def update_status(self, submission_id: int, status: str):
        submission = self.db.get(Submission, submission_id)

        if submission is None:
            return None

        submission.status = status

        self.db.commit()
        self.db.refresh(submission)

        return submission
from app.models.submission import Submission


def test_submission_default_values():
    submission = Submission(
        task_id=1,
        annotator_id=4,
        labels="positive",
    )

    assert submission.task_id == 1
    assert submission.annotator_id == 4
    assert submission.labels == "positive"
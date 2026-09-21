from app.database.connection import Base, engine

from app.models.user import User
from app.models.dataset import Dataset
from app.models.task import Task
from app.models.submission import Submission
from app.models.task_assignment import TaskAssignment
from app.models.annotation import Annotation
from app.models.dataset_version import DatasetVersion


Base.metadata.create_all(bind=engine)

print("DATABASE TABLES CREATED")
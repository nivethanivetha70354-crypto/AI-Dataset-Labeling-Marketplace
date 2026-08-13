from app.database.connection import Base, engine
from app.models.user import User
from app.models.dataset import Dataset
from app.models.task import Task

Base.metadata.create_all(bind=engine)

print("DATABASE TABLES CREATED")
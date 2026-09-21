from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import auth
from app.api import users
from app.api import datasets
from app.api import tasks
from app.api import submissions
from app.api import assignments
from app.api import ai
from app.api import annotations
from app.api import quality
from app.api import dataset_versions


app = FastAPI(
    title="AI Dataset Labeling Marketplace",
    description="API for dataset owners and annotators",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router)
app.include_router(users.router)
app.include_router(datasets.router)
app.include_router(tasks.router)
app.include_router(submissions.router)
app.include_router(assignments.router)
app.include_router(ai.router)
app.include_router(annotations.router)
app.include_router(quality.router)
app.include_router(dataset_versions.router)
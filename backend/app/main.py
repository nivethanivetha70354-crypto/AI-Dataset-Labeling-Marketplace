from fastapi import FastAPI

from app.api import auth, datasets, tasks, users

app = FastAPI(
    title="AI Dataset Labeling Marketplace API",
    version="1.0.0",
)

# API routers
app.include_router(auth.router)
app.include_router(datasets.router)
app.include_router(tasks.router)
app.include_router(users.router)


@app.get("/")
def root():
    return {
        "message": "AI Dataset Labeling Marketplace API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
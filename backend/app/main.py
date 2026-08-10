from fastapi import FastAPI

app = FastAPI(
    title="AI Dataset Labeling Marketplace API",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"message": "AI Dataset Labeling Marketplace API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
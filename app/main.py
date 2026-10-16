
from fastapi import FastAPI

app = FastAPI(
    title="DevOps CI/CD Platform",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "service": "devops-cicd-platform",
        "status": "running",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/version")
def version():
    return {"version": app.version}


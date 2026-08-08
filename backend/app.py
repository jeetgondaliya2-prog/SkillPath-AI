from fastapi import FastAPI

from backend.routes.profile import router as profile_router
from backend.routes.career import router as career_router
from backend.routes.roadmap import router as roadmap_router
from backend.routes.learning import router as learning_router


app = FastAPI(
    title="SkillPath AI",
    description="AI-powered career guidance platform",
    version="1.0.0"
)


# Profile routes
app.include_router(
    profile_router,
    prefix="/api"
)


# Career recommendation routes
app.include_router(
    career_router
)


# Roadmap routes
app.include_router(
    roadmap_router
)


# Learning resources routes
app.include_router(
    learning_router
)


@app.get("/")
def home():
    return {
        "message": "Welcome to SkillPath AI 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
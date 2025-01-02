from fastapi import FastAPI

from post_service.routes import router as post_router

app = FastAPI(
    title="Post Service",
    description="Service for managing posts in the system.",
    version="1.0.0",
)

app.include_router(post_router, prefix="/posts", tags=["Posts"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)

from fastapi import FastAPI
from app.api.endpoints import router

# Initialize FastAPI app
app = FastAPI(title="Receipt Processor", description="A simple receipt processor", version="1.0.0")

# Include API router
app.include_router(router)

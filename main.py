"""FastAPI application entry point."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import backend
from routers import frontend
from routers import login_backend

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(backend.router, prefix="/api")
app.include_router(frontend.router, prefix="/api")
app.include_router(login_backend.router, prefix="/api")

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from .auth import AuthMiddleware

def add_middlewares(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(AuthMiddleware)

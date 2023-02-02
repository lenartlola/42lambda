from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware

import os

from app.core.config import settings

from v1 import auth, api, user

def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)

    origins = [
        "http://127.0.0.1:3000",
        "http://localhost:3000",
        # The host should be allowed
    ]
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()
app.include_router(user.router)
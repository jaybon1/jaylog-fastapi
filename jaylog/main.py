from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .controller import join_controller

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(join_controller.router)

# app.router.redirect_slashes = False

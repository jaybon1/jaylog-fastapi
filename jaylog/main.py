from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from jaylog.controller import (join_controller, login_controller,
                               post_controller)
from jaylog.util import functions

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
app.include_router(login_controller.router)
app.include_router(post_controller.router)


@app.get("/")
async def test():
    return functions.res_generator()

# app.router.redirect_slashes = False

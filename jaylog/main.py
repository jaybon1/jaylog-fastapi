from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 엔티티 연관관계 호출하기 전에 엔티티들 먼저 import 해줘야 함
# 해당 파일에서 사용하지 않더라도 import 해줘야 함
# 최상단 파일에서 import 하여 어디든 사용 가능하도록 함
from jaylog.entity.like_entity import LikeEntity
from jaylog.entity.post_entity import PostEntity
from jaylog.entity.user_entity import UserEntity

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

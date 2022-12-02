from pydantic import BaseModel
from datetime import datetime


class ReqLoginDTO(BaseModel):
    id: str
    password: str


class ResLoginDTO(BaseModel):
    accessToken: str
    refreshToken: str


class JwtDTO(BaseModel):
    idx: int
    id: str
    simpleDesc: str
    profileImage: str
    role: str
    exp: datetime

    class Config:
        orm_mode = True

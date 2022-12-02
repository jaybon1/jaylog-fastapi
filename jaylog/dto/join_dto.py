from pydantic import BaseModel


class ReqJoinDTO(BaseModel):
    id: str
    password: str
    simpleDesc: str


class ResJoinDTO(BaseModel):
    idx: int

    class Config:
        orm_mode = True

from pydantic import BaseModel


class ReqJoinUserDTO(BaseModel):
    id: str
    password: str
    simpleDesc: str


class ResJoinUserDTO(BaseModel):
    idx: int

    class Config:
        orm_mode = True

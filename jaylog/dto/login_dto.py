from pydantic import BaseModel


class ReqLoginUserDTO(BaseModel):
    id: str
    password: str


class ResLoginUserDTO(BaseModel):
    idx: int
    id: str
    simpleDesc: str
    profileImage: str
    role: str

    class Config:
        orm_mode = True

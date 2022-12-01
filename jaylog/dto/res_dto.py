from pydantic import BaseModel


class ResDTO(BaseModel):
    code: int
    message: str = ""
    data: object | None = None

    # class Config:
    #     orm_mode = True

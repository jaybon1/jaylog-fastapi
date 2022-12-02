from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from jaylog.dependencies import get_db
from jaylog.dto.login_dto import Req
from jaylog.service import login_service

router = APIRouter(
    prefix="/login",
    tags=["login"]
)


@router.post("/")
async def login(reqDTO: Req, db: Session = Depends(get_db)) -> JSONResponse:
    return login_service.login(reqDTO, db)

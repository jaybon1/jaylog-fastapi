from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from jaylog.dependencies import get_db
from jaylog.dto.join_dto import Req
from jaylog.service import join_service

router = APIRouter(
    prefix="/join",
    tags=["join"]
)


@router.post("/")
async def join(reqDTO: Req, db: Session = Depends(get_db)) -> JSONResponse:
    return join_service.join(reqDTO, db)

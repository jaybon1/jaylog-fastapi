from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from ..dependencies import get_db
from ..dto.join_dto import ReqJoinUserDTO
from ..service import join_service

# from ..database.database import SessionLocal

router = APIRouter(
    prefix="/join",
    tags=["join"]
)


@router.post("/")
async def test(dto: ReqJoinUserDTO, db: Session = Depends(get_db)) -> JSONResponse:
    return join_service.join_user(dto, db)

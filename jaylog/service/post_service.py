from datetime import datetime
from sqlalchemy.orm import Session

from ..dto import post_dto
# 엔티티 연관관계 호출하기 전에 엔티티들 먼저 import 해줘야 함
# 사용하지 않더라도 import 해줘야 함
from ..entity.like_entity import LikeEntity
from ..entity.post_entity import PostEntity
from ..entity.user_entity import UserEntity
from ..util import functions

INTERNAL_SERVER_ERROR = {"code": 99, "message": "서버 내부 에러입니다."}


def get_posts(db: Session):
    postEntitys: list[PostEntity] = db.query(PostEntity).filter(
        PostEntity.delete_date == None).order_by(PostEntity.create_date.desc()).all()

    return functions.res_generator(content=list(map(post_dto.Res.toDTO, postEntitys)))

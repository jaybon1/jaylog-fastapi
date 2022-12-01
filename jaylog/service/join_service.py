from sqlalchemy.orm import Session
# 엔티티 연관관계 호출하기 전에 엔티티들 먼저 import 해줘야 함
from ..entity.user_entity import UserEntity
from ..entity.post_entity import PostEntity
from ..entity.like_entity import LikeEntity
from ..dto import join_dto
from datetime import datetime
from ..util import functions


USER_ID_EXIST_ERROR = {"code": 1, "message": "이미 존재하는 아이디입니다."}
INTERNAL_SERVER_ERROR = {"code": 99, "message": "서버 내부 에러입니다."}


def join_user(userDTO: join_dto.ReqJoinUserDTO, db: Session):

    userEntity: UserEntity = db.query(UserEntity).filter(
        UserEntity.id == userDTO.id).first()

    if (userEntity != None):
        return functions.res_generator(400, USER_ID_EXIST_ERROR)

    db_user = UserEntity(
        id=userDTO.id,
        password=userDTO.password,
        simple_desc=userDTO.simpleDesc if userDTO.simpleDesc else "한 줄 소개가 없습니다.",
        profile_image="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png",
        role="BLOGER",
        create_date=datetime.now(),
    )

    try:
        db.add(db_user)
        db.flush()
    except Exception as e:
        db.rollback()
        print(e)
        return functions.res_generator(status_code=500, error_dict=INTERNAL_SERVER_ERROR, data=e)
    finally:
        db.commit()

    db.refresh(db_user)

    return functions.res_generator(data=join_dto.ResJoinUserDTO(idx=db_user.idx))

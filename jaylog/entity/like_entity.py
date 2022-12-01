
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from datetime import datetime


from sqlalchemy import DateTime

from ..database.database import DBase


class LikeEntity(DBase):
    __tablename__ = "Like"

    idx = Column(Integer, primary_key=True, index=True)
    user_idx = Column(Integer, ForeignKey("User.idx"))
    post_idx = Column(Integer, ForeignKey("Post.idx"))
    create_date = Column(DateTime, default=datetime.now)
    update_date = Column(DateTime, onupdate=datetime.now)
    delete_date = Column(DateTime)

    user = relationship("UserEntity")

    post = relationship("PostEntity")

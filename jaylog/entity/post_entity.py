
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime


from sqlalchemy import DateTime

from ..database.database import DBase


class PostEntity(DBase):
    __tablename__ = "Post"

    idx = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    thumbnail = Column(String)
    content = Column(String)
    summary = Column(String)
    user_idx = Column(Integer, ForeignKey("User.idx"))
    create_date = Column(DateTime, default=datetime.now)
    update_date = Column(DateTime, onupdate=datetime.now)
    delete_date = Column(DateTime)

    user = relationship("UserEntity", back_populates="posts")

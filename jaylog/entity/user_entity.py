
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime


from sqlalchemy import DateTime

from ..database.database import DBase


class UserEntity(DBase):
    __tablename__ = "User"

    idx = Column(Integer, primary_key=True, index=True)
    id = Column(String, unique=True, index=True)
    password = Column(String)
    simple_desc = Column(String)
    profile_image = Column(String)
    role = Column(String)
    create_date = Column(DateTime, default=datetime.now)
    update_date = Column(DateTime, onupdate=datetime.now)
    delete_date = Column(DateTime)

    posts = relationship("PostEntity", back_populates="user")

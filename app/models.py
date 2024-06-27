from datetime import datetime
from typing import List

from app import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, DateTime, ForeignKey
from flask_login import UserMixin

class Post(db.Model):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), unique=True)
    content: Mapped[str] = mapped_column(Text)

    created: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updated: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(), onupdate=datetime.now())

    user_id = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates='posts')

    def __str__(self):
        return f"Post {self.id}: {self.title}"


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    nickname: Mapped[str] = mapped_column(String(25), unique=True)
    email: Mapped[str] = mapped_column(String(50), unique=True)
    password: Mapped[str] = mapped_column(String(50))

    posts: Mapped[List["Post"]] = relationship(back_populates='user')

    def __repr__(self):
        return f"User: {self.nickname}"

    def __str__(self):
        return self.nickname.capitalize()

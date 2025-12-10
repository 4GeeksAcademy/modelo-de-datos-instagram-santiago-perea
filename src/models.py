from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

class Follower(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    userfrom_id: Mapped["User"] = relationship()
    userto_id: Mapped["User"] = relationship()

class Media(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(nullable=False)
    url: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    post_id: Mapped["Post"] = relationship()

class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    password: Mapped[str] = mapped_column(nullable=False)

class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(nullable=False)
    author_id: Mapped["User"] = relationship()
    post_id: Mapped["Post"] = relationship()

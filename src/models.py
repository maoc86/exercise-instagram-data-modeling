import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(80), nullable=False, unique=True)
    firstname = Column(String(80), nullable=False)
    lastname = Column(String(80), nullable=False)
    email = Column(String(250), nullable=False, unique=True)

class Comment(Base):
    __tablename__ = 'comment'
    comment_id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))
    author_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    

class Post(Base):
    __tablename__ = 'post'
    post_id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


class Media(Base):
    __tablename__ = 'media'
    media_id = Column(Integer, primary_key=True)
    url = Column(String(300))
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

    


class Follower(Base):
    __tablename__ = 'follower'
    follower_id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

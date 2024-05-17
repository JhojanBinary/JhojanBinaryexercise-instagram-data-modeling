import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from enum import Enum

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50),nullable=False)
    firstname = Column(String(150),nullable = False)
    lastname= Column(String(150), nullable= False)
    email = Column(String(250), unique = True)


class Followers(Base):
    __tablename__ = 'followers'

    user_from_id = Column(Integer, ForeignKey('user.id'),primary_key=True)
    user_from_id_relationship = relationship(User)
    
    user_to_id = Column(Integer,ForeignKey('user.id'), primary_key = True)
    user_to_id_relationship = relationship(User)



class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True )
    user_id = Column(Integer,ForeignKey('user.id'))
    user_id_relationship = relationship(User)


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post_id_relationship = relationship(Post)


class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))


    author_id = Column(Integer, ForeignKey('user.id'))
    author_id_relationship = relationship(User)


    post_id = Column(Integer,ForeignKey('post.id'))
    post_id_relationship = relationship(Post)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

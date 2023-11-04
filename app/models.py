from .database_orm import Base
from sqlalchemy.sql.expression import Null
from sqlalchemy import Column,Integer,String ,ForeignKey
from sqlalchemy.orm import Session,relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP


class user_information(Base):
    __tablename__='user_information'

    id=Column(Integer,primary_key=True,nullable=False)
    password=Column(String,nullable=False)
    email=Column(String,nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    

    

class to_do(Base):
    __tablename__='to_do'

    task_id=Column(Integer,primary_key=True,nullable=False)
    task_title=Column(String,nullable=False)
    task_content=Column(String,nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    owner_id=Column(Integer,ForeignKey("user_information.id",ondelete="CASCADE"),nullable=False)

    owner=relationship('user_information')

class votes(Base):

    __tablename__='votes'

    todo_id=Column(Integer,ForeignKey('to_do.task_id',ondelete="CASCADE"),nullable=False,primary_key=True)
    user_id=Column(Integer,ForeignKey('user_information.id',ondelete="CASCADE"),nullable=False,primary_key=True)
    


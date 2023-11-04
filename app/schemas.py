from fastapi import FastAPI
from pydantic import BaseModel,conint
from sqlalchemy.sql.sqltypes import TIMESTAMP
from datetime import datetime
from typing import Optional


class user_info(BaseModel):
    
    password:str
    email: str
    

class user_send(BaseModel):
    
    id:int
    email: str
    # created_at:datetime
    class Config:
        orm_mode = True

class to_do_out(BaseModel):
    task_title: str
    task_content: str
    created_at: datetime
    owner: user_send

    class Config:
        orm_mode = True

class votes(BaseModel):
    todoid: int
    dir: conint(ge=0, le=1)


class to_do(BaseModel):
    
    task_title: str
    task_content:str


class Tokendata(BaseModel):
    id: Optional[str]= None


class results(BaseModel):
    task_title: str
    task_content: str
    created_at: datetime
   

    
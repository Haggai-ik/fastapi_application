from fastapi import FastAPI,Response,status,HTTPException,Depends
from .   import schemas
from .database_conn import connect
import psycopg2
from . import models
from psycopg2.extras import RealDictCursor
from .database_orm import engine,SessionLocal,Session,get_db
from passlib.context import CryptContext
from .routers import auth, users,todo,votes
models.Base.metadata.create_all(bind=engine)
cur,conn=connect()
app= FastAPI()


password_hash=CryptContext(schemes=['bcrypt'],deprecated='auto')


app.include_router(users.router)
app.include_router(todo.router)
app.include_router(auth.router)
app.include_router(votes.router)
     
#     db.add(todo)
#     db.commit()
#     db.refresh(todo)
#     return todo


    
'''
@app.get("/")
async def all_patients():
    cur.execute(""" select * from user_information """)
    posts=cur.fetchall()
    return posts

    



@app.get("/search_patient/{patient_id}")
async def get_patients(patient_id : int):
        cur.execute("""  select * from user_information where id = %s """,(patient_id,))
        patient=cur.fetchone()
        if patient ==None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='id not found')
        else:
             return patient'''
        


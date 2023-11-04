from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from .. import models,schemas,oath2
from app.database_orm  import Session,get_db
from typing import List
from sqlalchemy import func

router=APIRouter(tags=['todo'])

@router.post('/todo',status_code=status.HTTP_201_CREATED)
def create_todo(todo:schemas.to_do,db: Session = Depends(get_db),current_user =Depends(oath2.get_current_user)):
    todo=models.to_do(owner_id=current_user.id,**todo.dict())
    db.add(todo)
    db.commit()
    db.refresh(todo)
    print(current_user)
    return todo


@router.get('/todo/{todo_id}',status_code=status.HTTP_201_CREATED)
def get_todo(todo_id:int ,db: Session = Depends(get_db),current_user  =Depends(oath2.get_current_user)):
    todo= db.query(models.to_do).filter(models.to_do.task_id==todo_id).first()

    if todo==None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    if todo.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    
    return todo
     
#response_model=List[schemas.to_do_out]

@router.get("/todo")
async def get_all_users(db: Session = Depends(get_db),current_user  =Depends(oath2.get_current_user)):
    results=db.query(models.to_do,func.count(models.votes.todo_id).label('votes')).join(models.votes,models.votes.todo_id==models.to_do.task_id,isouter=True).group_by(models.to_do.task_id).all()
    #results = list ( map (lambda x : x._mapping, results))
    total= [result._mapping for result in results]
    return total
    
        
   
  
    
    
    




from fastapi import APIRouter,Depends,HTTPException,status
from .. import schemas
from .. import oath2,database_orm,models



router=APIRouter()

@router.post("/votes")
async def create_like(votes: schemas.votes, db : database_orm.Session=Depends(database_orm.get_db),current_user=Depends(oath2.get_current_user)):
    
    data_query=db.query(models.votes).filter(models.votes.todo_id==votes.todoid,models.votes.user_id==current_user.id).first()
    
    if votes.dir==1:
        if data_query:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT)
        data=models.votes(todo_id=votes.todoid,user_id=current_user.id)
        db.add(data)
        db.commit()
        return {'votes':'todo liked'}
    else:
        if not data_query:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT)
         
        data=db.query(models.votes).filter(models.votes.todo_id==votes.todoid,models.votes.user_id==current_user.id)
        data.delete(synchronize_session=False)
        db.commit()
        return {'todo':'todo unliked'}
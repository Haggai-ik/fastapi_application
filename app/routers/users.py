from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from .. import models,schemas
from app.database_orm  import Session,get_db
from passlib.context import CryptContext
from ..utils import hash_password

router=APIRouter(tags=['users'])

password_hash=CryptContext(schemes=['bcrypt'],deprecated='auto')

@router.get("/users")
async def get_all_users(db: Session = Depends(get_db)):
     all_users=db.query(models.user_information).all()
     for count,user_info in enumerate(all_users,start=1):
          # total=count+1
          # count=total
          total=count
     
     return{'total number of users': total}

@router.get("/users/{user}")
async def get_single_user(user:int, db: Session = Depends(get_db)):
     one_user=db.query(models.user_information).filter(models.user_information.id==user).first()
     if one_user==None:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='user_not_found')
     return one_user


@router.post("/users",status_code=status.HTTP_201_CREATED,response_model=schemas.user_send)
async def create_user(users:schemas.user_info,db: Session = Depends(get_db)):
     
    
    users.password=hash_password(users.password)
    # new_user=models.user_information(firstname=users.firstname,middlename=users.middlename,lastname=users.lastname,email=users.email)
    new_user=models.user_information(**users.dict())
    db.add(new_user)
    db.commit()
    #apply_leave.
    db.refresh(new_user)
 
    return new_user

@router.put("/users/{user}")
async def update_single_user(user:int,users:schemas.user_info,db: Session = Depends(get_db)):
     
    
    # new_user=models.user_information(firstname=users.firstname,middlename=users.middlename,lastname=users.lastname,email=users.email)
    user=db.query(models.user_information).filter(models.user_information.id==user)
    value=user.first()
    if value==None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    user.update(users.dict(),synchronize_session=False)
    
    db.commit()
    return {'message': 'new_user'}


@router.delete("/users/{user_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_single_user(user_id:int, db: Session = Depends(get_db)):
     
    
    # new_user=models.user_information(firstname=users.firstname,middlename=users.middlename,lastname=users.lastname,email=users.email)
    single_user=db.query(models.user_information).filter(models.user_information.id==user_id)
    value=single_user.first()
    if value==None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    print(value)
    single_user.delete(synchronize_session=False)
    
    db.commit()
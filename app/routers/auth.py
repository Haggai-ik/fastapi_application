from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from .. import models,schemas
from app.database_orm  import Session,get_db
from .. import schemas ,utils,oath2

from fastapi.security import OAuth2PasswordRequestForm



router=APIRouter(tags=['Authenticate'])


@router.post("/user_login",status_code=status.HTTP_200_OK)
async def user_login(user_info: OAuth2PasswordRequestForm =Depends() ,db: Session = Depends(get_db)):

    
    
    info=db.query(models.user_information).filter(models.user_information.email==user_info.username ).first()
    # user_info:schemas.user_info,
    # info=db.query(models.user_information).all()
    if not info:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    
    
    user_chect= utils.verify_password(user_info.password,info.password)
     
    if not user_chect:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    

    access_token= oath2.create_access_token(data={'user_id':info.id})

    return {'access_token':access_token,'token_type':'bearer'}
    



    
    
    

    print(user_chect)
    print(info)
    # if info==None:
    #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
   
    return info
   
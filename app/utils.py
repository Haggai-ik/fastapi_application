from passlib.context import CryptContext
password_hash=CryptContext(schemes=['bcrypt'],deprecated='auto')

def hash_password(user_password):

      hashed_password=password_hash.hash(user_password)
      return hashed_password


def verify_password(user_password,hashed_password):
      return password_hash.verify(user_password,hashed_password)


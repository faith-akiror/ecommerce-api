from passlib.context import CryptContext

pwd = CryptContext(schemes=["bcrypt"])

def hash_password(password):
    return pwd.hash(password)
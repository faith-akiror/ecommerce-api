from sqlalchemy.orm import Session
from app.db.models import User

def create_user(db: Session, email: str, password: str):
    user = User(email=email, password=password)
    db.add(user)
    db.commit()
    return user
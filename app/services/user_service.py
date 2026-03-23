from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate


class UserService:

    def get_all(self, db: Session):
        return db.query(User).all()

    def get_by_id(self, db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    def create(self, db: Session, user: UserCreate):
        db_user = User(
            name=user.name,
            account_number=user.account_number,
            news=[item.dict() for item in user.news] if user.news else None
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def update(self, db: Session, user_id: int, user_data: UserCreate):
        user = self.get_by_id(db, user_id)
        if not user:
            return None

        user.name = user_data.name
        user.account_number = user_data.account_number

        if user_data.news is not None:
            user.news = [item.dict() for item in user_data.news]

        db.commit()
        db.refresh(user)
        return user

    def delete(self, db: Session, user_id: int):
        user = self.get_by_id(db, user_id)
        if not user:
            return False

        db.delete(user)
        db.commit()
        return True
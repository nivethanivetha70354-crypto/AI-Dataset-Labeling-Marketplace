from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository


class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def get_all_users(self):
        return self.repository.get_all()

    def get_user_by_id(self, user_id: int):
        return self.repository.get_by_id(user_id)

    def get_user_by_email(self, email: str):
        return self.repository.get_by_email(email)

    def create_user(
        self,
        name: str,
        email: str,
        password: str,
        role: str,
    ):
        existing_user = self.repository.get_by_email(email)

        if existing_user:
            raise ValueError("User with this email already exists")

        user = User(
            name=name,
            email=email,
            password=password,
            role=role,
        )

        return self.repository.create(user)

    def delete_user(self, user: User):
        self.repository.delete(user)
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from typing import Optional, List
from domain.entities.user_entity import UserEntity
from application.ports.user_repository_port import UserRepositoryPort
from domain.exceptions.domain_exception import DomainException
from infrastructure.database.base import Base
from infrastructure.database.config import db

class UserTable(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, nullable=False)
    is_active = Column(Boolean, nullable=False)

class UserRepository(UserRepositoryPort):
    def create(self, user: UserEntity) -> UserEntity:

        if db.session.query(UserTable).filter_by(email=user.email).first():
            raise DomainException("Email already registered")

        record = UserTable(
            name=user.name,
            email=user.email,
            created_at=user.created_at,
            is_active=user.is_active
        )
        db.session.add(record)
        db.session.commit()
        return UserEntity(
            id=record.id,
            name=record.name,
            email=record.email,
            created_at=record.created_at,
            is_active=record.is_active
        )

    def get_by_id(self, user_id: int) -> Optional[UserEntity]:
        record = db.session.query(UserTable).filter_by(id=user_id).first()
        if not record:
            return None
        return UserEntity(
            id=record.id,
            name=record.name,
            email=record.email,
            created_at=record.created_at,
            is_active=record.is_active
        )

    def get_all(self) -> List[UserEntity]:
        records = db.session.query(UserTable).all()
        return [
            UserEntity(
                id=r.id,
                name=r.name,
                email=r.email,
                created_at=r.created_at,
                is_active=r.is_active
            )
            for r in records
        ]

    def update(self, user: UserEntity) -> UserEntity:
        record = db.session.query(UserTable).filter_by(id=user.id).first()
        if record:
            record.name = user.name
            record.email = user.email
            record.is_active = user.is_active
            db.session.commit()
        return UserEntity(
            id=record.id,
            name=record.name,
            email=record.email,
            created_at=record.created_at,
            is_active=record.is_active
        )

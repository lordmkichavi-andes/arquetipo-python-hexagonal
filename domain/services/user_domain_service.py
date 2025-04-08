from domain.entities.user_entity import UserEntity
from domain.exceptions.domain_exception import DomainException

class UserDomainService:
    def validate(self, user: UserEntity) -> None:
        if not user.name.strip():
            raise DomainException("Name cannot be empty")
        if "@" not in user.email:
            raise DomainException("Email is invalid")

    def activate(self, user: UserEntity) -> UserEntity:
        if not user.is_active:
            return UserEntity(
                id=user.id,
                name=user.name,
                email=user.email,
                created_at=user.created_at,
                is_active=True
            )
        return user

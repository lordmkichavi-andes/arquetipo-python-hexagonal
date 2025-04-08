from datetime import datetime
from domain.entities.user_entity import UserEntity
from domain.services.user_domain_service import UserDomainService
from application.ports.user_repository_port import UserRepositoryPort

class CreateUserUseCase:
    def __init__(self, repository: UserRepositoryPort):
        self.repository = repository
        self.domain_service = UserDomainService()

    def execute(self, name: str, email: str) -> UserEntity:
        user = UserEntity(
            id=0,
            name=name,
            email=email,
            created_at=datetime.utcnow(),
            is_active=False
        )
        self.domain_service.validate(user)
        return self.repository.create(user)

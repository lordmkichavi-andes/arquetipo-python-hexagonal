from typing import Optional, List
from domain.entities.user_entity import UserEntity
from application.ports.user_repository_port import UserRepositoryPort

class GetUserUseCase:
    def __init__(self, repository: UserRepositoryPort):
        self.repository = repository

    def get_by_id(self, user_id: int) -> Optional[UserEntity]:
        return self.repository.get_by_id(user_id)

    def get_all(self) -> List[UserEntity]:
        return self.repository.get_all()

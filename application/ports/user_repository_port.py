from abc import ABC, abstractmethod
from typing import Optional, List
from domain.entities.user_entity import UserEntity

class UserRepositoryPort(ABC):
    @abstractmethod
    def create(self, user: UserEntity) -> UserEntity:
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[UserEntity]:
        pass

    @abstractmethod
    def get_all(self) -> List[UserEntity]:
        pass

    @abstractmethod
    def update(self, user: UserEntity) -> UserEntity:
        pass

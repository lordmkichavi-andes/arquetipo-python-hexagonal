from application.use_cases.create_user_use_case import CreateUserUseCase
from domain.entities.user_entity import UserEntity

class MockRepo:
    def create(self, user: UserEntity) -> UserEntity:
        user.id = 99
        return user
    def get_by_id(self, user_id: int):
        return None
    def get_all(self):
        return []
    def update(self, user: UserEntity):
        return user

def test_create_user_use_case():
    repo = MockRepo()
    use_case = CreateUserUseCase(repo)
    user = use_case.execute("Charlie", "charlie@example.com")
    assert user.id == 99
    assert user.name == "Charlie"

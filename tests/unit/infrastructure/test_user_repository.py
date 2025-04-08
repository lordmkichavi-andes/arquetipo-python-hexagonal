from datetime import datetime

from domain.entities.user_entity import UserEntity
from infrastructure.adapters.user_repository import UserRepository


def test_user_repository(client):
    with client.application.app_context():
        repo = UserRepository()
        created = repo.create(UserEntity(id=0, name="Dave", email="dave@example.com", created_at=datetime.utcnow(), is_active=False))
        assert created.id == 1
        retrieved = repo.get_by_id(1)
        assert retrieved is not None
        assert retrieved.name == "Dave"
        all_users = repo.get_all()
        assert len(all_users) == 1
        updated = repo.update(UserEntity(id=1, name="Dave Updated", email="dave@update.com", created_at=retrieved.created_at, is_active=True))
        assert updated.name == "Dave Updated"
        assert updated.is_active

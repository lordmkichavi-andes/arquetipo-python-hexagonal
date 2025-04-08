from datetime import datetime
from domain.entities.user_entity import UserEntity

def test_user_entity():
    u = UserEntity(id=1, name="Test", email="test@example.com", created_at=datetime.utcnow(), is_active=False)
    assert u.name == "Test"
    assert not u.is_active

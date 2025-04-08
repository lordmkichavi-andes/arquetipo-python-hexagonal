import pytest
from datetime import datetime
from domain.entities.user_entity import UserEntity
from domain.services.user_domain_service import UserDomainService
from domain.exceptions.domain_exception import DomainException

def test_validate_valid_user():
    service = UserDomainService()
    user = UserEntity(id=1, name="Alice", email="alice@example.com", created_at=datetime.utcnow(), is_active=False)
    service.validate(user)

def test_validate_invalid_user():
    service = UserDomainService()
    user = UserEntity(id=1, name="   ", email="missing@", created_at=datetime.utcnow(), is_active=False)
    with pytest.raises(DomainException):
        service.validate(user)

def test_activate_user():
    service = UserDomainService()
    user = UserEntity(id=2, name="Bob", email="bob@example.com", created_at=datetime.utcnow(), is_active=False)
    activated = service.activate(user)
    assert activated.is_active

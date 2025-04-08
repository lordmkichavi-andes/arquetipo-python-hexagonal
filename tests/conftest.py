import pytest
from presentation.app import create_app
from infrastructure.database.config import db
from infrastructure.database.base import Base

@pytest.fixture
def app():
    app = create_app()
    app.config["TESTING"] = True
    return app

@pytest.fixture
def client(app):
    with app.test_client() as client:
        with app.app_context():
            Base.metadata.drop_all(db.engine)
            Base.metadata.create_all(db.engine)
        yield client

from flask import Flask
from application.use_cases.create_user_use_case import CreateUserUseCase
from application.use_cases.get_user_use_case import GetUserUseCase
from infrastructure.adapters.user_repository import UserRepository
from infrastructure.database.base import Base
from infrastructure.database.config import db
from infrastructure.error_handling.error_handler import register_error_handlers
from presentation.controllers.user_controller import user_bp, init_use_cases

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    with app.app_context():
        Base.metadata.create_all(db.engine)
        repo = UserRepository()
        init_use_cases(
            CreateUserUseCase(repo),
            GetUserUseCase(repo)
        )
    app.register_blueprint(user_bp)
    register_error_handlers(app)
    return app

if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5010)

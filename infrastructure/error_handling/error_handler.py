from flask import jsonify
from domain.exceptions.domain_exception import DomainException

def register_error_handlers(app):
    @app.errorhandler(DomainException)
    def handle_domain_exception(e):
        return jsonify({"error": str(e)}), 400

    @app.errorhandler(ValueError)
    def handle_value_error(e):
        return jsonify({"error": str(e)}), 400

    @app.errorhandler(404)
    def handle_not_found(e):
        return jsonify({"error": "Not found"}), 404

    @app.errorhandler(500)
    def handle_server_error(e):
        return jsonify({"error": "Server error"}), 500

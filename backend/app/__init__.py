from flask import (
    Flask,
    request,
    jsonify,
    abort
)
from .models import db, setup_db
from flask_cors import CORS
from .partido_controller import partido_bp
from .listas_controller import lista_bp
from config.local import config

def create_app(test_config=None):
    app = Flask(__name__)
    with app.app_context():
        CORS(app)
        app.register_blueprint(partido_bp)
        app.register_blueprint(lista_bp)
        setup_db(app, test_config['database_path'] if test_config else None)
        CORS(app, origins=['http://localhost:8080'])

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PATCH,POST,DELETE,OPTIONS')
        response.headers.add('Access-Control-Max-Age', '10')
        return response

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'message': 'Method not allowed'
        }), 405

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'message': 'Resource not found'
        }), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            'success': False,
            'message': 'Internal Server error'
        }), 500

    return app

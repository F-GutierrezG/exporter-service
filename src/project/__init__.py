import os
from flask import Flask
from flask_cors import CORS


def register_blueprints(app):
    from project.views.health import health_blueprint
    from project.views.users import users_blueprint

    app.register_blueprint(health_blueprint)
    app.register_blueprint(users_blueprint)


def create_app(script_info=None):
    app = Flask(__name__)

    CORS(app)

    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    register_blueprints(app)

    @app.shell_context_processor
    def ctx():
        return {'app': app}

    return app

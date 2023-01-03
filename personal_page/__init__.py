from typing import Any

from flask import Flask

from flask_cors import CORS


def init_app(config_file_path: str = "settings.py", **config: Any) -> Flask:
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_pyfile(config_file_path)
    app.config.update(**config)

    """ Initialize Plugins """
    CORS(app)

    """ Flask context """
    with app.app_context():
        # Include our Routes
        from .profile import profile_routes

        # Register Blueprints
        app.register_blueprint(profile_routes.profile_bp)

        return app

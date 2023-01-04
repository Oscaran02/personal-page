from typing import Any
import logging
from flask import Flask
from flask_cors import CORS


def init_app(config_file_path: str = "settings.py", **config: Any) -> Flask:
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_pyfile(config_file_path)
    app.config.update(**config)

    """Logging configuration"""
    logging.basicConfig(filename='./logs/logs.log', level=logging.DEBUG,
                        format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
    app.logger.info('Info level log')
    app.logger.warning('Warning level log')
    app.logger.error('Error level log')

    """ Initialize Plugins """
    CORS(app)

    """ Flask context """
    with app.app_context():
        # Include our Routes
        from .profile import routes

        # Register Blueprints
        app.register_blueprint(routes.profile_bp)

        return app

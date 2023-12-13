from src.framework.flask.create_flask_app import create_flask_app
from src.infrastructure.loggers.logger_default import LoggerDefault


logger = LoggerDefault()


if __name__ == "__main__":
    flask_memory_app = create_flask_app(logger)
    flask_memory_app.run(debug=True)

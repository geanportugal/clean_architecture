from framework.flask_app.create_flask_app import create_flask_app
from infrastructure.loggers.logger_default import LoggerDefault


logger = LoggerDefault()


if __name__ == "__main__":
    flask_memory_app = create_flask_app(logger)
    flask_memory_app.run(host="0.0.0.0", debug=True)

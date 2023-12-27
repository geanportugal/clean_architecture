from framework.fastapi_app.create_fastapi_app import create_fastapi_app
from infrastructure.loggers.logger_default import LoggerDefault


logger = LoggerDefault()


if __name__ == "__main__":
    fastapi_app = create_fastapi_app(logger)
    import uvicorn

    uvicorn.run(fastapi_app, host="0.0.0.0", port=5000)

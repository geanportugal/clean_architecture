from fastapi import FastAPI, HTTPException, Depends

from framework.fastapi_app.views.create_card_view import router
from interactor.interfaces.logger.logger import LoggerInterface
from interactor.errors.error_classes import FieldValueNotPermittedException
from infrastructure.db_models.db_base import Session as DBSession
from interactor.errors.error_classes import UniqueViolationError
from fastapi.responses import JSONResponse


def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()


def format_error_response(error: Exception, error_code: int, logger: LoggerInterface):
    """Format Error Response"""
    logger.log_exception(f"500 - Internal Server Error: {str(error)}")

    response = {
        "status_code": error_code,
        "error": error.__class__.__name__,
        "message": str(error),
    }
    return response, error_code


def create_fastapi_app(logger: LoggerInterface):
    logger = logger
    app = FastAPI()
    app.include_router(router, prefix="/api/V1", dependencies=[Depends(get_db)])

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request, exc):
        """Handle HTTP Exception Response"""
        logger.log_exception(str(exc.__class__.__name__))
        logger.log_exception(str(exc.detail))
        response = {
            "error": exc.__class__.__name__,
            "message": exc.detail,
        }
        return JSONResponse(content=response, status_code=exc.status_code)

    return app

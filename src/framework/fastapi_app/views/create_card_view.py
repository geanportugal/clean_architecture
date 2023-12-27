from fastapi import APIRouter, Depends
from infrastructure.loggers.logger_default import LoggerDefault
from fastapi.responses import JSONResponse
from framework.controllers.create_card_controller import CreateCardController

router = APIRouter()


@router.post("/card/", status_code=201)
async def create_card(input_json: dict):
    """Create Card FastAPI"""
    logger = LoggerDefault()
    controller = CreateCardController(logger)
    controller.get_card_info(input_json)
    result = controller.execute()
    result["id"] = str(result["id"])
    result["expiration_date"] = result["expiration_date"].isoformat()

    return JSONResponse(content=result)

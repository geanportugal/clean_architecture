from typing import Dict
from datetime import datetime
from interactor.use_cases.create_card import CreateCardUseCase
from infrastructure.repositories.card_repository import CardRepository
from interactor.dtos.create_card_dto import CreateCardInputDto
from framework.interfaces.controller_interface import ControllerInterface
from interactor.interfaces.logger.logger import LoggerInterface
from framework.presenters.create_card_presenter import CreateCardPresenter


class CreateCardController(ControllerInterface):
    """Create Card Controller Class"""

    def __init__(self, logger: LoggerInterface):
        self.logger = logger
        self.input_dto: CreateCardInputDto

    def get_card_info(self, json_input) -> None:
        """Get Card Info
        :param json_input: Input data
        :raises: ValueError if card param are missing.
        """

        if "number" in json_input:
            number = json_input["number"]
        else:
            raise ValueError("Missin Card Number")
        if "holder" in json_input:
            holder = json_input["holder"]
        else:
            raise ValueError("Missing Card Holder")

        if "cvv" in json_input:
            cvv = json_input["cvv"]
        else:
            cvv = None

        if "expiration_date" in json_input:
            expiration_date = json_input["expiration_date"]
        else:
            raise ValueError("Missing Card expiration_date")
        brand = None

        self.input_dto = CreateCardInputDto(number, holder, expiration_date, cvv, brand)

    def execute(self) -> Dict:
        """Execute the create card controller
        :returns: Card created
        """
        print("=====  controller  ======>")
        repository = CardRepository()
        presenter = CreateCardPresenter()
        use_case = CreateCardUseCase(presenter, repository, self.logger)
        result = use_case.execute(self.input_dto)
        return result

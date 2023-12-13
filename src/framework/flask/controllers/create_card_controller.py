from typing import Dict
from src.interactor.use_cases.create_card import CreateCardUseCase
from src.infrastructure.repositories.card_repository import CardRepository
from src.interactor.dtos.create_card_dto import CreateCardInputDto
from src.framework.flask.interfaces.controller_interface import ControllerInterface
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.framework.flask.presenters.create_card_presenter import CreateCardPresenter


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
        if "name" in json_input:
            name = json_input["name"]
        else:
            raise ValueError("Missing Profession Name")
        if "description" in json_input:
            description = json_input["description"]
        else:
            raise ValueError("Missing Profession Description")
        self.input_dto = CreateCardInputDto(name, description)

    def execute(self) -> Dict:
        """Execute the create profession controller
        :returns: Profession created
        """
        repository = CardRepository()
        presenter = CreateCardPresenter()
        use_case = CreateCardUseCase(presenter, repository, self.logger)
        result = use_case.execute(self.input_dto)
        return result

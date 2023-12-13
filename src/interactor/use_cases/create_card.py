from typing import Dict
from src.interactor.dtos.create_card_dto import CreateCardInputDto, CreateCardOutputDto
from src.interactor.interfaces.presenters.create_card_presenter import (
    CreateCardPresenterInterface,
)
from src.interactor.interfaces.repositories.card_repository import (
    CardRepositoryInterface,
)
from src.interactor.validations.create_card_validator import CreateCardInputDtoValidator
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.interactor.errors.error_classes import ItemNotCreatedException
from src.interactor.encryption.card_encryptor import CardEncryptor
from configs.config import SALT, SECRET_KEY_CARD


class CreateCardUseCase:
    """This class is responsible for creating a new card."""

    def __init__(
        self,
        presenter: CreateCardPresenterInterface,
        repository: CardRepositoryInterface,
        logger: LoggerInterface,
    ):
        self.presenter = presenter
        self.repository = repository
        self.logger = logger

    def execute(self, input_dto: CreateCardInputDto) -> Dict:
        """This method is responsible for creating a new card.
        :param input_dto: The input data transfer object.
        :type input_dto: CreateCardInputDto
        :return: Dict
        """

        validator = CreateCardInputDtoValidator(input_dto.to_dict())
        validator.validate()
        encryptor = CardEncryptor(SECRET_KEY_CARD, SALT)
        encryptor_number = encryptor.encrypt_card(input_dto.number).hex()
        card = self.repository.create(
            encryptor_number,
            input_dto.holder,
            input_dto.expiration_date,
            input_dto.cvv,
            input_dto.brand,
        )
        if card is None:
            self.logger.log_exception("Card creation failed")
            raise ItemNotCreatedException(input_dto.name, "Card")
        output_dto = CreateCardOutputDto(card)
        presenter_response = self.presenter.present(output_dto)
        self.logger.log_info("Card created successfully")
        return presenter_response

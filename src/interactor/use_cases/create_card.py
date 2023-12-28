from typing import Dict
import calendar
from datetime import date, datetime
from interactor.dtos.create_card_dto import CreateCardInputDto, CreateCardOutputDto
from interactor.interfaces.presenters.create_card_presenter import (
    CreateCardPresenterInterface,
)
from interactor.interfaces.repositories.card_repository import (
    CardRepositoryInterface,
)
from interactor.validations.create_card_validator import (
    CreateCardInputDtoValidator,
    ValidatedCreditCard,
)
from interactor.interfaces.logger.logger import LoggerInterface
from interactor.errors.error_classes import ItemNotCreatedException
from interactor.encryption.card_encryptor import CardEncryptor
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
        brand = ValidatedCreditCard(input_dto.number).get_brand()
        expiration_date = datetime.strptime(input_dto.expiration_date, "%m/%Y").date()
        lastday = calendar.monthrange(expiration_date.year, expiration_date.month)[1]

        expiration_date = expiration_date.replace(day=lastday)

        card = self.repository.create(
            encryptor_number,
            input_dto.holder,
            expiration_date,
            input_dto.cvv,
            brand,
        )
        if card is None:
            self.logger.log_exception("Card creation failed")
            raise ItemNotCreatedException(input_dto.name, "Card")
        output_dto = CreateCardOutputDto(card)
        presenter_response = self.presenter.present(output_dto)
        # self.logger.log_info(message="Card created successfully")

        return presenter_response

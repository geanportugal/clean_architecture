from typing import Dict
from interactor.dtos.create_card_dto import CreateCardOutputDto
from interactor.interfaces.presenters.create_card_presenter import (
    CreateCardPresenterInterface,
)


class CreateCardPresenter(CreateCardPresenterInterface):
    """Class for the CreateCardPresenter"""

    def present(self, output_dto: CreateCardOutputDto) -> Dict:
        """Present the CreateCard
        :param output_dto: CreateCardOutputDto
        :return: Dict
        """

        return {
            "id": output_dto.card.id,
            "number": output_dto.card.number,
            "holder": output_dto.card.holder,
            "expiration_date": output_dto.card.expiration_date.isoformat(),
            "cvv": output_dto.card.cvv,
            "brand": output_dto.card.brand,
        }

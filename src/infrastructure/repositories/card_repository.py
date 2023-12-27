""" Module for ProfessionPostgresqlRepository
"""

from typing import Optional
import uuid
from datetime import date
from sqlalchemy.exc import IntegrityError
from domain.entities.card import Card
from interactor.interfaces.repositories.card_repository import (
    CardRepositoryInterface,
)

from infrastructure.db_models.db_base import Session
from infrastructure.db_models.card_model import CardDBModel


class CardRepository(CardRepositoryInterface):
    """Postgresql Repository for Profession"""

    def __init__(self) -> None:
        self.__session = Session

    def __db_to_entity(self, db_row: CardDBModel) -> Optional[Card]:
        return Card(
            id=db_row.id,
            number=db_row.number,
            holder=db_row.holder,
            expiration_date=db_row.expiration_date,
            cvv=db_row.cvv,
            brand=db_row.brand,
        )

    def create(
        self,
        number: str,
        holder: str,
        expiration_date: date,
        cvv: Optional[str],
        brand: str,
    ) -> Optional[Card]:
        """Create Card
        :param number: str
        :param holder: str
        :param expiration_date: date
        :param cvv: str
        :param brand: str
        :return: Optional[Card]
        """
        id = uuid.uuid4()
        card_db_model = CardDBModel(
            id=id,
            number=number,
            holder=holder,
            expiration_date=expiration_date,
            cvv=cvv,
            brand=brand,
        )

        try:
            self.__session.add(card_db_model)
            self.__session.commit()
            self.__session.refresh(card_db_model)
        except IntegrityError as exception:
            raise (exception)

        if card_db_model is not None:
            return self.__db_to_entity(card_db_model)
        return None

    def get(self, id: uuid.UUID) -> Optional[Card]:
        """Get card by id
        :param id: uuid.uuid4
        :return: Optional[Card]
        """
        result = self.__session.query(CardDBModel).get(id)
        if result is not None:
            return self.__db_to_entity(result)
        return None

    def update(self, card: Card) -> Optional[Card]:
        """Update Card
        :param card: Card
        :return: Optional[Card]
        """
        card_db_model = CardDBModel(
            id=card.id,
            number=card.number,
            holder=card.holder,
            expiration_date=card.expiration_date,
            cvv=card.cvv,
            brand=card.brand,
        )
        result = (
            self.__session.query(CardDBModel)
            .filter_by(id=card.id)
            .update(
                {
                    "holder": card.holder,
                    "expiration_date": card.expiration_date,
                    "cvv": card.cvv,
                }
            )
        )
        if result == 0:
            return None
        self.__session.commit()
        return self.__db_to_entity(card_db_model)

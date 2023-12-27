import uuid
from datetime import date
from abc import ABC, abstractmethod
from typing import Optional
from domain.entities.card import Card


class CardRepositoryInterface(ABC):
    """This class is the interface for the CardRepository"""

    @abstractmethod
    def get(self, id: uuid.UUID) -> Optional[Card]:
        """Get a Card by id

        :param id: uuid.uui4()
        :return: Card
        """

    @abstractmethod
    def create(
        self,
        number: str,
        holder: str,
        expiration_date: date,
        cvv: Optional[str],
        brand: str,
    ) -> Optional[Card]:
        """Create a Card

        :param number: Card Number
        :param holder: Card Holder
        :param expiration_date: Card Expiration Date
        :param cvv: Card cvv
        :param brand: card brand
        :return: Id
        """
        print("===== repository =====>")

    @abstractmethod
    def update(self, card: Card) -> Optional[Card]:
        """Save a Card

        :param Card: Card
        :return: Card
        """

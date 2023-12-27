from typing import Dict
from abc import ABC, abstractmethod
from interactor.dtos.create_card_dto import CreateCardOutputDto


class CreateCardPresenterInterface(ABC):
    """Class for the Interface of the CardPresenter"""

    @abstractmethod
    def present(self, output_dto: CreateCardOutputDto) -> Dict:
        """Present the Card"""
        print("==== presenter ====>")

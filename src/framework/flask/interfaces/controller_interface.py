from typing import Dict
from abc import ABC, abstractmethod


class ControllerInterface(ABC):
    def get_card_info(self, json_input) -> None:
        """Get Card Info
        :param json_input: Input data
        :raises: ValueError if card param are missing.
        """

    @abstractmethod
    def execute(self) -> Dict:
        """Executes the controller
        :returns: Card created
        """

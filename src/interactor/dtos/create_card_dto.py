from dataclasses import dataclass, asdict
from typing import Optional
from datetime import date
from domain.entities.card import Card


@dataclass
class CreateCardInputDto:
    number: str
    holder: str
    expiration_date: str
    cvv: Optional[str]
    brand: Optional[str]

    def to_dict(self):
        """Convert data into dictionary"""
        print("=== dto input ====>")
        return asdict(self)


@dataclass
class CreateCardOutputDto:
    """Output Dto for create card"""

    print("=== dto output ====>")

    card: Card

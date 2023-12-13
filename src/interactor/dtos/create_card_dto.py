from dataclasses import dataclass, asdict
from typing import Optional
from datetime import datetime
from src.domain.entities.card import Card


@dataclass
class CreateCardInputDto:
    number: str
    holder: str
    expiration_date: datetime
    cvv: Optional[str]
    brand: str

    def to_dict(self):
        """Convert data into dictionary"""
        return asdict(self)


@dataclass
class CreateCardOutputDto:
    """Output Dto for create card"""

    card: Card

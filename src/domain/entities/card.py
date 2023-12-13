import uuid
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional


@dataclass
class Card:
    """Definition of the Card entity"""

    id: uuid.UUID
    number: str
    holder: str
    expiration_date: datetime
    cvv: Optional[str]
    brand: str

    @classmethod
    def from_dict(cls, data):
        """Convert data from a dictionary"""
        return cls(**data)

    def to_dict(self):
        """Convert data into dictionary"""
        return asdict(self)

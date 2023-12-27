import uuid
from datetime import date
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from infrastructure.db_models.db_base import Base


class CardDBModel(Base):
    """Defines the Card database model."""

    __tablename__ = "card"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    number: Mapped[str] = mapped_column(String(255), nullable=False)
    holder: Mapped[str] = mapped_column(String(80), nullable=False)
    expiration_date: Mapped[date] = mapped_column(nullable=False)
    cvv: Mapped[str] = mapped_column(String(4), nullable=True)
    brand: Mapped[str] = mapped_column(String(16), nullable=False)

from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    Sequence,
    ForeignKey,
    Text,
    func
)
from swagger_server.models.db import Base


class MovilizationStatus(Base):
    __tablename__ = "movilization_status"
    __table_args__ = {"schema": "technical"}

    id_status = Column(
        Integer,
        Sequence("movilization_status_id_seq", schema="technical"),
        primary_key=True,
        nullable=False
    )

    name = Column(
        Text,
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    updated_at = Column(
        DateTime,
        server_default=func.now()
    )

    created_by = Column(
        Text,
    )

    updated_by = Column(
        Text,
    )

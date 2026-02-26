from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    Sequence,
    ForeignKey,
    func
)
from swagger_server.models.db import Base


class MovilizationReason(Base):
    __tablename__ = "movilization_reason"
    __table_args__ = {"schema": "technical"}

    id_movilization_reason = Column(
        Integer,
        Sequence("movilization_reason_id_seq", schema="technical"),
        primary_key=True,
        nullable=False
    )

    movilization_id = Column(
        Integer,
        ForeignKey("technical.movilization_control.id_movilization"),
        nullable=False
    )

    reason_id = Column(
        Integer,
        ForeignKey("technical.reasons_movilization.id_reason"),
        nullable=False
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

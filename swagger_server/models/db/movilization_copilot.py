from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    Sequence,
    ForeignKey,
    func
)
from swagger_server.models.db import Base


class MovilizationCopilot(Base):
    __tablename__ = "movilization_copilot"
    __table_args__ = {"schema": "technical"}

    id_movilization_copilot = Column(
        Integer,
        Sequence("movilization_copilot_id_seq", schema="technical"),
        primary_key=True,
        nullable=False
    )

    movilization_id = Column(
        Integer,
        ForeignKey("technical.movilization_control.id_movilization"),
        nullable=False
    )

    copilot_id = Column(
        Integer,
        ForeignKey("technical.vehicle_copilot.id_copilot"),
        nullable=False
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

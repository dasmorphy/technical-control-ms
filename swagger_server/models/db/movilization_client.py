from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    Sequence,
    ForeignKey,
    func
)
from swagger_server.models.db import Base


class MovilizationClient(Base):
    __tablename__ = "movilization_client"
    __table_args__ = {"schema": "technical"}

    id_movilization_client = Column(
        Integer,
        Sequence("movilization_client_id_seq", schema="technical"),
        primary_key=True,
        nullable=False
    )

    movilization_id = Column(
        Integer,
        ForeignKey("technical.movilization_control.id_movilization"),
        nullable=False
    )

    client_project_id = Column(
        Integer,
        ForeignKey("technical.client_projects.id_client_projects"),
        nullable=False
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

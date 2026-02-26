from sqlalchemy import (
    Column,
    Boolean,
    Integer,
    Text,
    DateTime,
    Sequence,
    func
)
from swagger_server.models.db import Base


class ClientProject(Base):
    __tablename__ = "client_project"
    __table_args__ = {"schema": "technical"}

    id_client_projects = Column(
        Integer,
        Sequence("client_projects_id_seq", schema="technical"),
        primary_key=True,
        nullable=False
    )

    name = Column(
        Text,
        nullable=False
    )

    is_active = Column(Boolean, default=True)


    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )

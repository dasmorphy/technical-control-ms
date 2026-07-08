from sqlalchemy import (
    Column,
    Boolean,
    ForeignKey,
    Integer,
    Text,
    DateTime,
    Sequence,
    func
)
from swagger_server.models.db import Base


class TaskLocation(Base):
    __tablename__ = "task_location"
    __table_args__ = {"schema": "technical"}

    id_task_location = Column(
        Integer,
        Sequence("task_location_id_seq", schema="technical"),
        primary_key=True,
        nullable=False
    )

    location_id = Column(
        Integer,
        ForeignKey("technical.clients_location.id_location")
    )

    task_id = Column(
        Integer,
        ForeignKey("technical.task_technical.id_task")
    )

    created_by = Column(Text)
    updated_by = Column(Text)

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )

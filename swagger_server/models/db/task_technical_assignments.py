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
from sqlalchemy.dialects.postgresql import UUID

class TaskTechnicalAssignment(Base):
    __tablename__ = "task_technical_assignments"
    __table_args__ = {"schema": "technical"}

    id_assignment = Column(
        Integer,
        Sequence("task_technical_assignments_id_seq", schema="technical"),
        primary_key=True,
        nullable=False
    )

    task_id = Column(
        Integer,
        ForeignKey("technical.task_technical.id_task")
    )

    user_tech_id = Column(
        UUID(as_uuid=True),
        ForeignKey("public.users.id_user")
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )

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


class TaskTechnical(Base):
    __tablename__ = "task_technical"
    __table_args__ = {"schema": "technical"}

    id_task = Column(
        Integer,
        Sequence("task_technical_id_seq", schema="technical"),
        primary_key=True,
        nullable=False
    )

    name = Column(Text)
    description = Column(Text)
    code = Column(Text)
    

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

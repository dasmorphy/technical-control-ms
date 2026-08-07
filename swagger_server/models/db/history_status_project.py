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


class HistoryStatusProject(Base):
    __tablename__ = "history_status_project"
    __table_args__ = {"schema": "technical"}

    id_history = Column(
        Integer,
        Sequence("history_status_project_id_seq", schema="technical"),
        primary_key=True,
        nullable=False
    )

    tech_task_id = Column(
        Integer,
        ForeignKey("technical.task_technical.id_task")
    )

    commentary = Column(Text)

    created_by = Column(Text)

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

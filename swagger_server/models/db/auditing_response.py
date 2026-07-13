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


class AuditingResponse(Base):
    __tablename__ = "auditing_response"
    __table_args__ = {"schema": "technical"}

    id_response = Column(
        Integer,
        Sequence("auditing_item_id_seq", schema="technical"),
        primary_key=True,
        nullable=False
    )

    auditing_id = Column(
        Integer,
        ForeignKey("technical.auditing.id_auditing")
    )

    item_id = Column(
        Integer,
        ForeignKey("technical.auditing_item.id_item")
    )

    response = Column(Text)
    observation = Column(Text)

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

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


class AuditingSections(Base):
    __tablename__ = "auditing_sections"
    __table_args__ = {"schema": "technical"}

    id_section = Column(
        Integer,
        Sequence("auditing_sections_id_seq", schema="technical"),
        primary_key=True,
        nullable=False
    )

    name = Column(Text)
    order_number = Column(Integer)

    created_by = Column(Text)

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

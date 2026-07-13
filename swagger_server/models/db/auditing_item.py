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


class AuditingItem(Base):
    __tablename__ = "auditing_item"
    __table_args__ = {"schema": "technical"}

    id_item = Column(
        Integer,
        Sequence("auditing_item_id_seq", schema="technical"),
        primary_key=True,
        nullable=False
    )

    section_id = Column(
        Integer,
        ForeignKey("technical.auditing_sections.id_section")
    )

    name = Column(Text)
    order_number = Column(Integer)

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

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


class AuditingSignaturesImg(Base):
    __tablename__ = "auditing_signatures_img"
    __table_args__ = {"schema": "technical"}

    id_image = Column(
        Integer,
        Sequence("auditing_signatures_id_seq", schema="technical"),
        primary_key=True,
        nullable=False
    )

    auditing_id = Column(
        Integer,
        ForeignKey("technical.auditing.id_auditing")
    )

    auditor_path = Column(Text)
    responsible_path = Column(Text)
    client_path = Column(Text)

    created_at = Column(
        DateTime,
        server_default=func.now()
    )
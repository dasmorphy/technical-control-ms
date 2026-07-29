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


class AuditingFindingsImg(Base):
    __tablename__ = "auditing_findings_img"
    __table_args__ = {"schema": "technical"}

    id_image = Column(
        Integer,
        Sequence("auditing_findings_img_id_seq", schema="technical"),
        primary_key=True,
        nullable=False
    )

    finding_auditing_id = Column(
        Integer,
        ForeignKey("technical.auditing_findings.id_finding")
    )

    img_path = Column(Text)

    created_at = Column(
        DateTime,
        server_default=func.now()
    )
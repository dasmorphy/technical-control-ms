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


class AuditingFinding(Base):
    __tablename__ = "auditing_findings"
    __table_args__ = {"schema": "technical"}

    id_finding = Column(
        Integer,
        Sequence("auditing_findings_id_seq", schema="technical"),
        primary_key=True,
        nullable=False
    )

    auditing_id = Column(
        Integer,
        ForeignKey("technical.auditing.id_auditing")
    )


    description = Column(Text)
    criticality = Column(Text)

    responsible = Column(Text)
    commitment = Column(Text)

    created_at = Column(
        DateTime,
        server_default=func.now()
    )
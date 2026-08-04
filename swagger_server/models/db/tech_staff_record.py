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


class TechStaffRecord(Base):
    __tablename__ = "tech_staff_record"
    __table_args__ = {"schema": "technical"}

    id_staff_record = Column(
        Integer,
        Sequence("tech_staff_record_id_seq", schema="technical"),
        primary_key=True,
        nullable=False
    )

    record_id = Column(
        Integer,
        ForeignKey("technical.technical_record.id_record")
    )

    tech_staff_id = Column(
        Integer,
        ForeignKey("technical.technical_staff.id_technical")
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

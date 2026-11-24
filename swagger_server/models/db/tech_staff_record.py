from sqlalchemy import (
    UUID,
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

    # Registro de campo de un Soporte / Asistencia (proxy-glpi-ms /register-technical);
    # en ese caso record_id es NULL
    inspection_id = Column(
        Integer,
        ForeignKey("internal_management.inspection_technical.id_inspection")
    )

    management_technical_id = Column(
        Integer,
        ForeignKey("internal_management.technical_ticket_management.id_management_technical")
    )

    tech_staff_id = Column(
        Integer,
        ForeignKey("technical.technical_staff.id_technical")
    )

    user_tech_id = Column(
        UUID(as_uuid=True),
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

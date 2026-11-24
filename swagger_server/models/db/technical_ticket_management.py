from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Sequence, Text, func

from swagger_server.models.db import Base


class TechnicalTicketManagement(Base):
    """Gestión técnica y registros técnicos de campo de Soportes / Asistencias.
    Los escribe proxy-glpi-ms (/register-technical); aquí solo se leen para unir
    los registros de campo (is_field_record = true) con technical_record."""

    __tablename__ = "technical_ticket_management"
    __table_args__ = {"schema": "internal_management"}

    id_management_technical = Column(
        Integer,
        Sequence("technical_ticket_management_id_seq", schema="internal_management"),
        primary_key=True,
        nullable=False,
    )

    inspection_id = Column(
        Integer,
        ForeignKey("internal_management.inspection_technical.id_inspection"),
    )

    code_management = Column(Text)
    description = Column(Text)
    status = Column(Text)
    vehicle = Column(Text)
    record_status = Column(Text)
    is_field_record = Column(Boolean, nullable=False, server_default="false", default=False)

    created_by = Column(Text)
    updated_by = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

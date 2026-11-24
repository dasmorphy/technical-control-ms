from sqlalchemy import Column, DateTime, ForeignKey, Integer, Text, func

from swagger_server.models.db import Base


class InspectionDocuments(Base):
    """Documentos de la inspección (proxy-glpi-ms); solo lectura. Las imágenes de
    un registro de campo tienen su management_technical_id."""

    __tablename__ = "inspection_documents"
    __table_args__ = {"schema": "internal_management"}

    id_document = Column(Integer, primary_key=True, autoincrement=True)

    inspection_id = Column(
        Integer,
        ForeignKey("internal_management.inspection_technical.id_inspection"),
    )

    management_technical_id = Column(
        Integer,
        ForeignKey("internal_management.technical_ticket_management.id_management_technical"),
    )

    document_path = Column(Text)
    name_document = Column(Text)
    type_document = Column(Text)
    created_at = Column(DateTime, server_default=func.now())

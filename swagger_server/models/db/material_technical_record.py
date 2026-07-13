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


class MaterialTechnicalRecord(Base):
    __tablename__ = "material_technical_record"
    __table_args__ = {"schema": "technical"}

    id_material_record = Column(
        Integer,
        Sequence("material_technical_record_id_seq", schema="technical"),
        primary_key=True,
        nullable=False
    )

    record_id = Column(
        Integer,
        ForeignKey("technical.technical_record.id_record")
    )

    quantity = Column(Integer)
    material = Column(Text)

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )

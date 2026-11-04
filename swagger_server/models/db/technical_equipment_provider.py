from sqlalchemy import (
    Column,
    Integer,
    Sequence,
    ForeignKey
)
from swagger_server.models.db import Base


class TechnicalEquipmentProvider(Base):
    __tablename__ = "technical_equipment_provider"
    __table_args__ = {"schema": "technical"}

    id_equipment_provider = Column(
        Integer,
        Sequence("technical_equipment_provider_id_seq", schema="technical"),
        primary_key=True,
        nullable=False
    )

    equipment_id = Column(
        Integer,
        ForeignKey("technical.technical_equipment.id_equipment"),
        nullable=False
    )

    provider_id = Column(
        Integer,
        ForeignKey("internal_management.providers_products.id_provider"),
        nullable=False
    )

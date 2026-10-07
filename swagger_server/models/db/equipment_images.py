from swagger_server.models.db import Base
from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    Sequence,
    String,
    Text,
    Time,
    ForeignKey,
    func
)


class EquipmentImages(Base):
    __tablename__ = 'equipment_images'
    __table_args__ = {'schema': 'internal_management'}

    id_image = Column(
        Integer,
        Sequence(
            "equipment_images_id_seq",
            schema="internal_management",
        ),
        primary_key=True,
    )

    equipment_tech_id = Column(
        Integer,
        ForeignKey('technical.technical_equipment.id_equipment', onupdate='NO ACTION', ondelete='NO ACTION'),
    )

    image_path = Column(Text)

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
    Sequence,
    ForeignKey,
    func
)
from swagger_server.models.db import Base


class MovilizationImages(Base):
    __tablename__ = "movilization_images"
    __table_args__ = {"schema": "technical"}

    id_image = Column(
        Integer,
        Sequence("movilization_images_id_seq", schema="technical"),
        primary_key=True,
        nullable=False
    )

    movilization_id = Column(
        Integer,
        ForeignKey("technical.movilization_control.id_movilization"),
        nullable=False
    )

    image_path = Column(Text)

    type = Column(Text)

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

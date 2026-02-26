from sqlalchemy import (
    Column,
    Boolean,
    Integer,
    Text,
    DateTime,
    Sequence,
    func
)
from swagger_server.models.db import Base


class VehicleDriver(Base):
    __tablename__ = "vehicle_driver"
    __table_args__ = {"schema": "technical"}

    id_driver = Column(
        Integer,
        Sequence("vehicle_driver_id_seq", schema="technical"),
        primary_key=True,
        nullable=False
    )

    name = Column(
        Text,
        nullable=False
    )

    is_active = Column(Boolean, default=True)

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )

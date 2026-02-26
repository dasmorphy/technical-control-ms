from sqlalchemy import (
    Column,
    Integer,
    Text,
    Time,
    DateTime,
    Sequence,
    ForeignKey,
    func
)
from swagger_server.models.db import Base


class MovilizationControl(Base):
    __tablename__ = "movilization_control"
    __table_args__ = {"schema": "technical"}

    id_movilization = Column(
        Integer,
        Sequence("movilization_control_id_seq", schema="technical"),
        primary_key=True,
        nullable=False
    )

    exit_date = Column(Time)

    arrival_date = Column(
        Time,
        server_default=func.now()
    )

    license_id = Column(
        Integer,
        ForeignKey("technical.vehicle_license.id_license")
    )

    initial_km = Column(Text)

    final_km = Column(Text)

    final_gasoline = Column(Text)

    initial_gasoline = Column(Text)

    destiny = Column(Text)

    exit_point = Column(Text)

    driver_id = Column(
        Integer,
        ForeignKey("technical.vehicle_driver.id_driver")
    )

    observations = Column(Text)

    created_at = Column(
        Time,
        server_default=func.now()
    )

    updated_at = Column(
        Time,
        server_default=func.now(),
        onupdate=func.now()
    )

    created_by = Column(Text)

    updated_by = Column(Text)

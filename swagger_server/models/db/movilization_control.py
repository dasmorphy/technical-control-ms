from sqlalchemy import (
    Boolean,
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

    exit_date = Column(DateTime)

    arrival_date = Column(
        DateTime,
        server_default=func.now()
    )

    license_id = Column(
        Integer,
        ForeignKey("technical.vehicle_license.id_license")
    )

    initial_km = Column(Text)

    final_km = Column(Text)

    final_gasoline_id = Column(
        Integer,
        ForeignKey("technical.level_gasoline.id_level")
    )

    initial_gasoline_id = Column(
        Integer,
        ForeignKey("technical.level_gasoline.id_level")
    )

    destiny = Column(Text)

    exit_point = Column(Text)

    driver_id = Column(
        Integer,
        ForeignKey("technical.vehicle_driver.id_driver")
    )

    status = Column(
        Integer,
        ForeignKey("technical.movilization_status.id_status")
    )

    have_incident = Column(Boolean, default=False)

    detail_incident = Column(Text)

    observations = Column(Text)

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )

    created_by = Column(Text)

    updated_by = Column(Text)

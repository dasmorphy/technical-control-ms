from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
    Sequence,
    func
)
from swagger_server.models.db import Base


class TechnicalStaff(Base):
    __tablename__ = "technical_staff"
    __table_args__ = {"schema": "technical"}

    id_technical = Column(
        Integer,
        Sequence("technical_staff_id_seq", schema="technical"),
        primary_key=True,
        nullable=False
    )

    name = Column(Text)

    created_by = Column(Text)
    updated_by = Column(Text)

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )

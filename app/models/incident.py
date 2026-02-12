from sqlalchemy import Column, Integer, Float, Boolean, DateTime, Enum
from sqlalchemy.sql import func

from app.db.base import Base
from app.models.enums import SystemType, ComponentType, ErrorType


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)

    system = Column(Enum(SystemType), nullable=False)
    component = Column(Enum(ComponentType), nullable=False)
    error_type = Column(Enum(ErrorType), nullable=False)

    duration_seconds = Column(Integer, nullable=False)
    frequency_last_24h = Column(Integer, nullable=False)
    load = Column(Float, nullable=False)

    deployment_recent = Column(Boolean, default=False)
    affected_users = Column(Integer, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

from sqlalchemy import Column, Integer, Float, DateTime, Enum, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base
from app.models.enums import FailureType, SeverityLevel


class AnalysisResult(Base):
    __tablename__ = "analysis_results"

    id = Column(Integer, primary_key=True, index=True)

    incident_id = Column(Integer, ForeignKey("incidents.id"), nullable=False)

    probable_cause = Column(Enum(FailureType), nullable=False)
    confidence = Column(Float, nullable=False)
    severity = Column(Enum(SeverityLevel), nullable=False)

    score_breakdown = Column(JSON, nullable=False)
    similar_incidents = Column(Integer, default=0)

    analyzed_at = Column(DateTime(timezone=True), server_default=func.now())

    incident = relationship("Incident")

from app.db.database import engine
from app.db.base import Base

from app.models.incident import Incident
from app.models.analysis_result import AnalysisResult

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.services.analyzer import analyze_incident

app = FastAPI(title="Failure Classification API", version="1.0")

# Pydantic model para validar input
class Incident(BaseModel):
    system: str
    component: str
    error_type: str
    duration_seconds: int
    frequency_last_24h: int
    load: float
    deployment_recent: bool
    affected_users: int

@app.post("/incidents/analyze")
def analyze(incident: Incident):
    # Converter pydantic object para dict
    incident_dict = incident.dict()

    # Chama o motor de análise
    result = analyze_incident(incident_dict)

    return result

# Endpoint teste
@app.get("/")
def root():
    return {"message": "Failure Classification API is running"}

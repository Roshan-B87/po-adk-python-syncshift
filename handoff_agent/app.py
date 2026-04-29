"""
handoff_agent — A2A application entry point.

Start the server with:
    uvicorn handoff_agent.app:a2a_app --host 0.0.0.0 --port 8004

The agent card is served publicly at:
    GET http://localhost:8004/.well-known/agent-card.json
"""
import os

from a2a.types import AgentSkill
from shared.app_factory import create_a2a_app

from .agent import root_agent

a2a_app = create_a2a_app(
    agent=root_agent,
    name="handoff_agent",
    description=(
        "An ICU Shift Handoff Copilot that creates comprehensive SBAR summaries "
        "by simultaneously fetching demographics, vitals, medications, and conditions."
    ),
    url=os.getenv("HANDOFF_AGENT_URL", os.getenv("BASE_URL", "http://localhost:8004")),
    port=8004,
    fhir_extension_uri=f"{os.getenv('PO_PLATFORM_BASE_URL', 'http://localhost:5139')}/schemas/a2a/v1/fhir-context",
    skills=[
        AgentSkill(
            id="patient-handoff",
            name="patient-handoff",
            description="Generate a complete shift handoff summary including risk score.",
            tags=["handoff", "summary", "fhir", "sbar"],
        ),
    ],
    require_api_key=False,
)

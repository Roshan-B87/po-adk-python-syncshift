"""
handoff_agent — Zero-Click Shift Handoff Copilot.

This agent uses the get_patient_handoff_data tool to pull all FHIR data in one go
and generates a structured SBAR handoff summary.
"""
from google.adk.agents import Agent

from shared.fhir_hook import extract_fhir_context
from shared.tools import get_patient_handoff_data

root_agent = Agent(
    name="handoff_agent",
    model="gemini-1.5-flash",
    description=(
        "An ICU Shift Handoff Copilot that creates comprehensive SBAR summaries "
        "by simultaneously fetching demographics, vitals, medications, and conditions."
    ),
    instruction=(
        "You are an expert ICU Nursing and Physician Shift-Handoff Copilot. "
        "When asked for a patient summary or handoff, call the 'get_patient_handoff_data' tool. "
        "Using the bulk data returned, output a strictly formatted clinical summary using the "
        "SBAR standard (Situation, Background, Assessment, Recommendation). "
        "1. Situation: Patient name, age, gender, and the computed risk score. "
        "2. Background: Key past conditions and active medications. "
        "3. Assessment: Current vitals logic and any critical abnormalities. "
        "4. Recommendation: Recommended follow up and whether the risk score warrants immediate attention. "
        "5. Data Provenance: You MUST conclude your report by explicitly citing your data sources. Clearly state which facts came from the 'FHIR Database' and which came from 'Uploaded Clinical Notes'. "
        "Keep it highly professional, precise, and medical. Do not guess any data. Clinical safety is paramount."
    ),
    tools=[
        get_patient_handoff_data,
    ],
    before_model_callback=extract_fhir_context,
)

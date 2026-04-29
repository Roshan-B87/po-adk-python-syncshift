import os
import sys
import asyncio
from google.adk.tools import ToolContext

# Mock tool context
class MockState:
    def __init__(self):
        self.state = {
            "fhir_url": "https://hapi.fhir.org/baseR4",
            "fhir_token": "mock-token",
            "patient_id": "12345"
        }
    def get(self, key, default=None):
        return self.state.get(key, default)

class MockToolContext:
    def __init__(self):
        self.state = MockState().state

from shared.tools.fhir import get_patient_handoff_data

try:
    ctx = MockToolContext()
    res = get_patient_handoff_data(ctx)
    print("SUCCESS: get_patient_handoff_data returned correctly.")
except Exception as e:
    import traceback
    traceback.print_exc()
    sys.exit(1)

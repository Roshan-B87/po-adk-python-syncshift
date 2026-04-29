# 🏥 SyncShift AI
**The Zero-Click Clinical Handoff Copilot**

## 📖 The Problem: "Pajama Time" & Medical Errors
During hospital shift changes, doctors and nurses spend hours digging through scattered Electronic Health Records (EHR) to brief the incoming team. This manual data gathering leads to physician burnout (often called "Pajama Time") and increases the risk of critical information being missed during handoffs. 

## 💡 What Our Project Does
**SyncShift AI** is a specialized Generative AI agent built for the Prompt Opinion platform. Instead of hunting through tabs, a clinician simply asks the agent for a handoff summary. 

In seconds, our Python backend connects to the hospital's FHIR server and simultaneously fetches:
* Patient Demographics
* Active Medications
* Underlying Conditions
* Recent Vitals

It then computes a real-time **Patient Risk Score** and uses **Gemini 1.5 Flash** to synthesize this raw data into a professional, structured **SBAR (Situation, Background, Assessment, Recommendation)** clinical summary.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Framework:** Google ADK (Agent Development Kit), A2A SDK (Agent-to-Agent Protocol), FastAPI/Starlette (via Uvicorn)
* **LLM:** Google Gemini 1.5 Flash (via Google AI Studio)
* **Healthcare Data Standard:** FHIR R4 (Fast Healthcare Interoperability Resources)
* **Infrastructure:** ngrok (for local tunneling)

---

## 🚀 How to Run the Project Locally

Follow these exact steps to run the agent on your Windows machine and connect it to the Prompt Opinion platform.

### Step 1: Set Up the Environment
Make sure you have activated your virtual environment and installed the dependencies.
```bash
# Activate the virtual environment
.\.venv\Scripts\activate

# Install the required dependencies (Make sure a2a-sdk is <1.0.0)
pip install -r requirements.txt
```

### Step 2: Configure Environment Variables
Create a `.env` file in the root directory and add the following:
```env
# Your Google AI Studio API Key
GOOGLE_API_KEY=your-api-key-here

# We use standard Gemini, not Vertex AI
GOOGLE_GENAI_USE_VERTEXAI=FALSE
```

### Step 3: Start the Python Server
Run the Uvicorn server to start the agent on port 8004.
```bash
uvicorn handoff_agent.app:a2a_app --host 0.0.0.0 --port 8004
```
*Keep this terminal window open!*

### Step 4: Open the ngrok Tunnel
Because Prompt Opinion is on the internet, it needs a secure tunnel to reach your local laptop. Open a **brand new terminal window** and run:
```bash
ngrok http 8004
```
Copy the `https://...ngrok-free.app` URL that appears on your screen.

### Step 5: Update the .env file with your ngrok URL
Go back to your `.env` file and add the URL you just copied:
```env
BASE_URL=https://your-unique-url.ngrok-free.app
HANDOFF_AGENT_URL=https://your-unique-url.ngrok-free.app
```
**Important:** Restart your Python server (Ctrl+C, then run the uvicorn command again) so it picks up the new URL!

### Step 6: Connect to Prompt Opinion
1. Go to **app.promptopinion.ai**
2. Add a new **Independent A2A Agent**.
3. Set the **URL** to your ngrok URL.
4. Leave the API Key blank (or use `my-secret-key-123` if required).
5. Click Save.

### Step 7: Test the Agent
Open a chat in Prompt Opinion, ensure a synthetic patient is actively selected in the UI, and send this prompt:
> *"I'm about to take over the shift for this patient. Give me a complete SBAR clinical handoff summary and calculate their risk score."*

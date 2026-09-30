import os
import sys
import uuid
import datetime
from typing import List, Optional
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from psgcas_data import (
    PSGCAS_INFO,
    FAQS,
    PLACEMENT_RULES,
    MOCK_INTERVIEW_QUESTIONS,
    get_fallback_response
)

# Optional Gemini Integration
GEMINI_AVAILABLE = False
try:
    from google import genai
    from google.genai import types
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False

app = FastAPI(
    title="PSGCAS Placement & Career AI Assistant API",
    description="Backend API for PSG College of Arts and Science Placement & Career Guidance Cell",
    version="1.0.0"
)

# Enable CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-Memory Storage for Rectification Tickets
TICKETS_DB = []

# Pydantic Schemas
class ChatMessage(BaseModel):
    message: str
    stream: Optional[str] = "General"
    session_id: Optional[str] = None

class RectifyTicketRequest(BaseModel):
    student_name: str
    roll_number: str
    department: str
    email: str
    phone: str
    query_category: str
    issue_description: str

class MockInterviewRequest(BaseModel):
    stream: str
    count: Optional[int] = 4

# Initialize Gemini Client if API Key is present
gemini_client = None
if GEMINI_AVAILABLE:
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key:
        try:
            gemini_client = genai.Client(api_key=api_key)
            print("[INFO] Gemini AI Client initialized successfully.")
        except Exception as e:
            print(f"[WARNING] Failed to initialize Gemini Client: {e}")


SYSTEM_INSTRUCTION = f"""
You are the official AI Placement & Career Guidance Assistant for PSG College of Arts and Science (PSGCAS), Coimbatore.
College Name: {PSGCAS_INFO['college_name']}
Location: {PSGCAS_INFO['location']}
Office: {PSGCAS_INFO['office_location']}
Contact Email: {PSGCAS_INFO['contacts']['email']} / {PSGCAS_INFO['contacts']['training_email']}
Phone: {PSGCAS_INFO['contacts']['phone']}
Recruiters: 200+ annual recruiters (Deloitte, EY, PwC, TCS, Cognizant, Infosys, Wipro, Amazon, Goldman Sachs, Biocon, etc.)
Statistics: 2,100+ offers/year, package range ₹3.5 LPA - ₹12 LPA.

Your Guidelines:
1. Provide warm, polite, accurate, and professional responses tailored for college students.
2. Structure answers using markdown headings, bullet points, and bold text for readability.
3. Address queries regarding placement registration (5th sem UG / 3rd sem PG), SEED training, eligibility, recruiter expectations, resume writing, and interview prep.
4. If a query requires official administrative correction (e.g. mark sheet discrepancy, portal bug, or dispute), guide the student to use the "Rectify Query" option in this application.
"""

@app.get("/api/health")
def health_check():
    return {
        "status": "online",
        "college": PSGCAS_INFO["college_name"],
        "gemini_active": gemini_client is not None,
        "timestamp": datetime.datetime.now().isoformat()
    }

@app.get("/api/info")
def get_info():
    return {
        "psgcas_info": PSGCAS_INFO,
        "rules": PLACEMENT_RULES
    }

@app.get("/api/faqs")
def get_faqs():
    return {"faqs": FAQS}

@app.post("/api/chat")
def chat_endpoint(payload: ChatMessage):
    user_msg = payload.message.strip()
    if not user_msg:
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    # Try Gemini API if configured
    if gemini_client:
        try:
            response = gemini_client.models.generate_content(
                model="gemini-2.5-flash",
                contents=user_msg,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_INSTRUCTION,
                    temperature=0.7,
                )
            )
            if response and response.text:
                return {
                    "response": response.text,
                    "engine": "Gemini AI Engine",
                    "timestamp": datetime.datetime.now().isoformat()
                }
        except Exception as err:
            print(f"[NOTICE] Gemini API call fallback: {err}")

    # Fallback to PSGCAS Local Knowledge Engine
    fallback_text = get_fallback_response(user_msg)
    return {
        "response": fallback_text,
        "engine": "PSGCAS CDC Intelligent Knowledge Engine",
        "timestamp": datetime.datetime.now().isoformat()
    }

@app.post("/api/mock-interview")
def generate_mock_interview(payload: MockInterviewRequest):
    stream = payload.stream
    questions = MOCK_INTERVIEW_QUESTIONS.get(stream, MOCK_INTERVIEW_QUESTIONS["General HR"])
    return {
        "stream": stream,
        "questions": questions,
        "instructions": "Practice answering each question out loud. Focus on the STAR method (Situation, Task, Action, Result) for behavioral & technical queries."
    }

@app.post("/api/rectify-query")
def submit_rectify_ticket(payload: RectifyTicketRequest):
    ticket_id = f"PSGCAS-CDC-{uuid.uuid4().hex[:6].upper()}"
    created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    ticket = {
        "ticket_id": ticket_id,
        "student_name": payload.student_name,
        "roll_number": payload.roll_number,
        "department": payload.department,
        "email": payload.email,
        "phone": payload.phone,
        "query_category": payload.query_category,
        "issue_description": payload.issue_description,
        "status": "Submitted & Pending Review by CDC Coordinator",
        "created_at": created_at
    }
    
    TICKETS_DB.append(ticket)
    
    return {
        "success": True,
        "message": f"Query rectifying request successfully submitted under Ticket ID {ticket_id}.",
        "ticket": ticket
    }

@app.get("/api/tickets")
def list_tickets():
    return {
        "count": len(TICKETS_DB),
        "tickets": TICKETS_DB
    }

# Serve Frontend static assets
frontend_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontend")
if os.path.exists(frontend_dir):
    app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

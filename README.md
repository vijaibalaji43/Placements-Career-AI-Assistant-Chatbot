# PSG College of Arts and Science (PSGCAS) - Placement & Career AI Web Chatbot

An AI-powered web application created for the **Career Development Center (CDC)** at **PSG College of Arts and Science (PSGCAS), Coimbatore**. This platform enables students to resolve placement-related doubts, understand eligibility requirements, practice stream-specific mock interviews, review resumes, and escalate/rectify unresolved grievances directly to CDC staff.

---

## 🌟 Key Features

1. **PSGCAS Academic Branding & Interface**:
   - PSGCAS Deep Navy & Gold color palette.
   - Live CDC status badge and quick contact information (Ground Floor, C-Block, `cdc@psgcas.ac.in`).

2. **AI Doubt Solver (Dual Engine)**:
   - Real-time response generation via **Google Gemini API** (`gemini-2.5-flash`).
   - Built-in **PSGCAS Knowledge Base Engine** fallback that functions without needing API keys or network connection.
   - Quick topic chips: *Placement Registration*, *Top Recruiters & CTC*, *SEED Training Details*, *CGPA & Backlog Rules*, *Rectify Registration Error*.

3. **Mock Interview Simulator**:
   - Tailored practice questions for **Computer Science / IT / BCA**, **Commerce / BBA**, **Science / Biotech**, and **General HR**.
   - In-app practice workspace with answer hints and STAR method tips.

4. **AI Resume Analyzer**:
   - Instant feedback on formatting, action verbs, and skill alignment for campus recruitment drives.

5. **Rectify & Escalate Query Hub**:
   - Formal ticket generation system for portal errors, mark sheet disputes, and eligibility clarifications.
   - Generates trackable Ticket IDs (e.g., `PSGCAS-CDC-XXXXXX`).

6. **Placement FAQs**:
   - Interactive categorised accordion covering registration rules, eligibility criteria, SEED training, and one-student-one-job policies.

---

## 🚀 How to Run the Application

### Option 1: One-Click Python Launcher (Recommended)
```bash
python run.py
```
This automatically installs required dependencies and opens your browser at `http://127.0.0.1:8000`.

### Option 2: Manual FastAPI Launch
1. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```
2. Start Uvicorn web server:
   ```bash
   python -m uvicorn backend.app:app --reload --port 8000
   ```
3. Open `http://localhost:8000` in your web browser.

---

## 🔑 (Optional) Setting Google Gemini API Key

To enable live Google Gemini AI model generation, set your API key environment variable before starting:

**On Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY="your_actual_gemini_api_key"
python run.py
```

*Note: If no API key is set, the chatbot automatically uses the built-in PSGCAS CDC Knowledge Base.*

---

## 📁 Project Structure

```
College Placements and Career Chatbot/
├── backend/
│   ├── app.py                # FastAPI web backend & API endpoints
│   ├── psgcas_data.py        # PSGCAS Placement & Career Knowledge Base & FAQs
│   └── requirements.txt      # Python dependencies
├── frontend/
│   ├── index.html            # Main Web Chat UI for PSGCAS Students
│   ├── css/
│   │   └── style.css         # Styling with PSGCAS branding (Navy & Gold)
│   └── js/
│       └── app.js            # Main chat logic, API integration, & UI state
├── run.py                    # One-click launcher script
└── README.md                 # Complete documentation
```

---

## 🏫 Contact & Support
- **Office**: Career Development Center (CDC), Ground Floor, C-Block, PSGCAS Campus, Coimbatore – 641018.
- **Email**: `cdc@psgcas.ac.in` / `seedtraining@psgcas.ac.in`
- **Phone**: 0422 – 430 3421

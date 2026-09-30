"""
PSG College of Arts and Science (PSGCAS) - Career Development Center (CDC)
Knowledge Base & Frequently Asked Questions Data Store
"""

PSGCAS_INFO = {
    "college_name": "PSG College of Arts and Science (PSGCAS)",
    "location": "Avinashi Road, Civil Aerodrome Post, Coimbatore – 641018, Tamil Nadu, India",
    "department": "Career Development Center (CDC)",
    "office_location": "C-Block, Ground Floor, PSGCAS Campus",
    "contacts": {
        "email": "cdc@psgcas.ac.in",
        "training_email": "seedtraining@psgcas.ac.in",
        "phone": "0422 – 430 3421",
        "working_hours": "Monday to Friday: 9:00 AM - 5:00 PM"
    },
    "statistics": {
        "annual_recruiters": "200+ top companies",
        "annual_offers": "2,100+ placement offers made per year",
        "average_package": "₹3.5 LPA - ₹5.0 LPA",
        "highest_package": "₹10 LPA - ₹12 LPA"
    }
}

FAQS = [
    {
        "id": "faq-1",
        "category": "Registration & Eligibility",
        "question": "How do I register for campus placements at PSGCAS?",
        "answer": "Placement registration opens at the beginning of the 5th semester for UG programs and 3rd semester for PG programs. Students must fill out the CDC Career Option Questionnaire via the student portal, selecting 'Campus Placement' as their goal. Ensure all semester marksheets are updated in your portal."
    },
    {
        "id": "faq-2",
        "category": "Registration & Eligibility",
        "question": "What are the general eligibility criteria for placement drives?",
        "answer": "Standard criteria vary by recruiting company:\n- **Tier-1 / IT & Product MNCs**: 60% or 6.5+ CGPA with no standing backlogs.\n- **Consulting / Core Science / Commerce**: 60%-75% aggregate marks with clear academic record.\n- **General Open Drives**: 50%+ or passing grade, max 1-2 active backlogs allowed by select recruiters.\n*Always check individual company notification details sent by CDC.*"
    },
    {
        "id": "faq-3",
        "category": "Training & SEED",
        "question": "What is SEED Training provided by PSGCAS?",
        "answer": "SEED stands for **Skill Enhancement & Employability Development**. It is a structured training program organized by CDC:\n- **Year 1 & 2**: Life skills, verbal ability, communication, and quantitative aptitude.\n- **Final Year**: Advanced placement training including Resume Building, Technical Mock Interviews, Group Discussions (GD), and Company-Specific Orientation."
    },
    {
        "id": "faq-4",
        "category": "Recruiters & Companies",
        "question": "Which top companies recruit from PSGCAS?",
        "answer": "PSGCAS hosts 200+ premier recruiters across various streams:\n- **Big 4 & Consulting**: Deloitte, EY (Ernst & Young), PwC, KPMG.\n- **IT & Tech Services**: TCS, Cognizant, Infosys, Wipro, Accenture, HCL, LTI Mindtree.\n- **Commerce, Banking & Analytics**: Goldman Sachs, HSBC, ICICI Bank, HDFC Bank, Pickyourtrail, Mu Sigma.\n- **Science & Healthcare**: Biocon, Syngene, Dr. Reddy's, Zifo R&D, Cipla, Pfizer."
    },
    {
        "id": "faq-5",
        "category": "Rules & Policy",
        "question": "What is the One-Student-One-Job policy at PSGCAS CDC?",
        "answer": "Under the CDC placement policy, once a student secures a job offer above a certain slab (e.g. Dream / Core company offer), they are considered 'Placed' and are ineligible for further drive registrations, ensuring fair opportunities for all candidates. Exceptions apply for 'Dream Tier' upgrades if approved by CDC."
    },
    {
        "id": "faq-6",
        "category": "Internships & PPO",
        "question": "Are internships compulsory and can they lead to full-time jobs (PPO)?",
        "answer": "For programs like MCA, MSc, MBA, and B.Com (PA/Honours), internships are an integral curriculum component. CDC assists in securing corporate internships. High performance during internship often leads to Pre-Placement Offers (PPOs) before final semester drives commence."
    },
    {
        "id": "faq-7",
        "category": "Doubts & Escalation",
        "question": "What if my question isn't answered or I have a specific portal issue?",
        "answer": "If you have specific portal errors, eligibility disputes, or document submission queries, you can submit a ticket using the **'Rectify Query'** tab in this web app or visit C-Block CDC Office (0422 - 430 3421 / cdc@psgcas.ac.in)."
    }
]

PLACEMENT_RULES = [
    "Formal business attire or official college uniform is mandatory for all placement drives.",
    "Students must carry 3 printed copies of their resume, college ID card, passport photos, and all semester marksheets.",
    "Punctuality is strictly enforced; late arrivals will result in debarment from the recruitment drive.",
    "Misbehavior, proxy attendance, or fake credential submission leads to immediate expulsion from CDC activities."
]

MOCK_INTERVIEW_QUESTIONS = {
    "General HR": [
        "Tell me about yourself and why you chose your branch at PSGCAS.",
        "What are your greatest strengths and areas you are currently improving?",
        "Where do you see yourself in 3 years after graduating from PSGCAS?",
        "Why do you want to join our company over other recruiters visiting campus?"
    ],
    "Computer Science / IT / BCA": [
        "Explain the difference between Object-Oriented Programming (OOP) concepts with real-world examples.",
        "How does a SQL JOIN work? Differentiate between INNER, LEFT, and RIGHT JOIN.",
        "What is REST API and how does HTTP status code 200 differ from 404 and 500?",
        "Explain the basic time complexity of Binary Search vs Linear Search."
    ],
    "Commerce / BBA / Economics": [
        "Explain the fundamental difference between Financial Accounting and Management Accounting.",
        "What are the 3 main financial statements, and how are they interconnected?",
        "How do interest rate changes by RBI impact commercial banking sector in India?",
        "What is working capital management and why is it vital for corporate liquidity?"
    ],
    "Science / Biotechnology / Chemistry": [
        "Describe standard quality assurance / quality control (QA/QC) protocols in lab analysis.",
        "Explain PCR (Polymerase Chain Reaction) steps and its industrial/diagnostic applications.",
        "How do you prepare a buffer solution of a specific pH?",
        "What safety procedures are essential when handling hazardous bio-reagents?"
    ]
}


def get_fallback_response(user_query: str) -> str:
    """
    Intelligent pattern-matching fallback response engine tailored for PSGCAS CDC.
    Executes when external LLM API is unavailable.
    """
    query_lower = user_query.lower().strip()
    
    # Check for greeting
    if any(w in query_lower for w in ["hi", "hello", "hey", "greetings", "good morning", "good afternoon"]):
        return (
            "Hello! Welcome to the **PSG College of Arts and Science (PSGCAS) Placement & Career AI Assistant**! 🎓\n\n"
            "I can help you with:\n"
            "• **Placement Registration & Eligibility**\n"
            "• **SEED Training Program Details**\n"
            "• **Visiting Companies & Package Stats**\n"
            "• **CDC Policy & Rules**\n"
            "• **Rectifying & Escalating Unresolved Doubts**\n\n"
            "What would you like to ask today?"
        )
    
    # Registration / Process
    if any(w in query_lower for w in ["register", "registration", "apply", "process", "portal", "questionnaire"]):
        return (
            "### 📝 PSGCAS Placement Registration Process\n\n"
            "1. **Eligibility Window**: Begins during the 5th semester (UG) and 3rd semester (PG).\n"
            "2. **Career Questionnaire**: Log in to your PSGCAS student portal and complete the CDC Career Option form.\n"
            "3. **Document Verification**: Upload verified semester marksheets, updated CV, and ID credentials.\n"
            "4. **Drive Alerts**: Registered students will receive drive notifications, criteria, and deadline alerts via email & student portal.\n\n"
            "Need help with a specific portal issue? Use the **Rectify Query** tab on the left navigation bar!"
        )

    # Companies / Recruiters
    if any(w in query_lower for w in ["company", "companies", "recruiter", "deloitte", "tcs", "ey", "infosys", "wipro", "package", "salary", "lpa"]):
        return (
            "### 🏢 PSGCAS Recruiters & Placement Statistics\n\n"
            "PSGCAS hosts over **200+ recruiters** annually, securing **2,100+ offers**!\n\n"
            "**Key Recruiters by Sector:**\n"
            "- **Big 4 & Finance**: Deloitte, EY, PwC, KPMG, Goldman Sachs, ICICI, HDFC\n"
            "- **IT & Services**: TCS, Cognizant, Infosys, Wipro, Accenture, Amazon, HCL\n"
            "- **Pharma & Science**: Biocon, Syngene, Dr. Reddy's, Zifo R&D\n\n"
            "**Salary Packages:**\n"
            "- **Highest Package**: ₹10 - ₹12 LPA\n"
            "- **Average / Median Package**: ₹3.5 LPA - ₹5.0 LPA"
        )

    # SEED / Training
    if any(w in query_lower for w in ["seed", "train", "training", "aptitude", "gd", "group discussion", "resume", "prep"]):
        return (
            "### 🎯 SEED (Skill Enhancement & Employability Development)\n\n"
            "PSGCAS CDC offers comprehensive SEED training across your academic tenure:\n"
            "- **1st & 2nd Year**: Communication skills, quantitative aptitude, verbal reasoning, and personal grooming.\n"
            "- **Final Year**: Intensive placement preparation including mock technical/HR interviews, CV review workshops, and company-specific test series.\n\n"
            "📩 Contact SEED Cell: `seedtraining@psgcas.ac.in`"
        )

    # Contact / Location / Office
    if any(w in query_lower for w in ["contact", "email", "phone", "location", "office", "cdc", "where"]):
        return (
            "### 📍 PSGCAS CDC Contact Details\n\n"
            "**Career Development Center (CDC)**\n"
            "- **Location**: Ground Floor, C-Block, PSGCAS Campus, Coimbatore – 641018\n"
            "- **Email**: `cdc@psgcas.ac.in` / `seedtraining@psgcas.ac.in`\n"
            "- **Phone**: 0422 – 430 3421\n"
            "- **Working Hours**: Monday – Friday, 9:00 AM – 5:00 PM"
        )

    # Eligibility / CGPA / Backlog
    if any(w in query_lower for w in ["eligibility", "cgpa", "backlog", "criteria", "percentage", "marks"]):
        return (
            "### 📊 Eligibility Criteria Guidelines\n\n"
            "- **Tier 1 / MNCs**: Minimum 60% or 6.5+ CGPA without active backlogs.\n"
            "- **Core & Consulting Companies**: 65%-75% aggregate marks requirement.\n"
            "- **Mass Drives**: 50%-60% aggregate; select companies allow up to 1-2 standing backlogs.\n"
            "*Detailed company-wise eligibility is announced prior to each drive on the CDC notification board.*"
        )

    # Escalation / Rectify / Issue
    if any(w in query_lower for w in ["rectify", "doubt", "issue", "complain", "grievance", "ticket", "help", "escalate"]):
        return (
            "### 🛠️ Need to Rectify an Issue?\n\n"
            "If you have an unresolved grievance, incorrect portal data, or specific queries not listed here:\n"
            "1. Click on the **'Rectify Query'** tab in the sidebar.\n"
            "2. Fill in your Roll Number, Department, and detailed issue description.\n"
            "3. Submit to generate a tracking Ticket ID. Our CDC coordinators will address it within 24-48 hours!"
        )

    # Generic Fallback response with helpful suggestions
    return (
        f"Thank you for reaching out to **PSGCAS Placement AI** regarding: *\"{user_query}\"*.\n\n"
        "Here are key resources to assist you:\n"
        "- **CDC Office**: C-Block, PSGCAS Campus (`cdc@psgcas.ac.in` | Phone: 0422-430 3421)\n"
        "- **Registration Window**: Opened for 5th sem (UG) & 3rd sem (PG) on the PSGCAS Student Portal.\n"
        "- **SEED Training**: Skill workshops conducted regularly by CDC.\n\n"
        "💡 *Tip: If your issue requires official correction or human intervention, click on **'Rectify Query'** in the side navigation menu to submit a ticket directly to the Placement Cell!*"
    )

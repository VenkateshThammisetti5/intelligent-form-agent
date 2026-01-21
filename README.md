# Intelligent Form Agent

An AI-powered document processing system designed to handle both standard identity documents and unstructured generic forms using the Groq LPU Inference Engine. This agent provides specialized extraction for Aadhaar forms and advanced analysis for other generic forms.

---

## Overview
The Intelligent Form Agent acts as a dual-mode gatekeeper and analyst for PDF documents:
* **Standard Identity Mode:** Uses strict validation to ensure only Aadhaar documents are processed, extracting specific fields like Resident Name and DOB etc.
* **Generic Analysis Mode:** Processes unstructured documents (like hospital or bank forms) to provide summaries, data extraction, and question-answering based strictly on the provided context.

---

## Pipeline Architecture
The system operates through a structured three-tier pipeline:
1.  **Ingestion (Streamlit & PyMuPDF):** The user uploads one or multiple PDFs. The `fitz` (PyMuPDF) library extracts raw text from each page.
2.  **Reasoning (Groq & Llama-3.1):** * **Standard Gatekeeper:** Validates identity documents and extracts a fixed set of fields.
    * **Generic Analyst:** Detects user intent (Summary, Extraction, or Q&A) and applies strict anti-hallucination rules.
3.  **Output (Streamlit UI):** Results are displayed side-by-side for identity forms or as markdown for generic analysis.

---

🛠️ Environment Setup
1. Prerequisites
Python: 3.9+
API Key: Groq Cloud Account
2. Installation
bash
pip install streamlit pymupdf groq
Use code with caution.

3. API Configuration
OS	Command
Windows	set GROQ_API_KEY=gsk_your_key_here
Linux / macOS	export GROQ_API_KEY=gsk_your_key_here
🚀 Execution Guide
Navigate to Project Root
bash
cd intelligent-form-agent
Use code with caution.

Launch the Orchestrator
bash
python src/run.py
Use code with caution.

Access the Dashboard
URL: http://localhost:8501
📽️ Project Demonstration
The project demo is hosted externally due to file size limits.
Link: View Demo Folder:https://drive.google.com/file/d/1J6rkpziZbjxXUGUkkAIF9SbcGhSHqNgP/view?usp=sharing
📋 Usage & Expected Outputs
Scenario A: Standard Identity Forms
Input: Upload Aadhaar PDF → Click "Extract All Data"
Output:
yaml
Aadhaar Number: 1234-5678-9012
Resident Name: John Doe
Gender: Male
DOB: 01/01/1990
Address: 123 Maple St, Delhi
Use code with caution.

Scenario B: Generic Forms (Hospital/Bank)
Query	Expected Behavior
"Summarize report"	Returns a 3-4 point bulleted list (-).
"Blood pressure?"	Returns specific value or "Information not found".
"Extract all"	Returns a clean list of every key-value pair found.
⚙️ Design Architecture
🛡️ Strict Mode Rules: The agent automatically rejects hospital/bank forms in the Standard tab to prevent data cross-contamination.
🎯 Zero Temperature: The LLM is locked at temperature=0 to ensure 100% factual consistency and zero hallucination.
⚡ In-Memory Processing: Uses PyMuPDF for lightning-fast text extraction before sending to the LLM.






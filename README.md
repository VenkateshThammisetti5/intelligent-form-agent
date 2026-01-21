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

🛠 Environment Setup
1. Prerequisites
Python 3.9+
Groq API Key: Obtain one from the Groq Cloud Console.
2. Installation
Install the necessary dependencies using pip:
bash
pip install streamlit pymupdf groq
Use code with caution.

3. Configure API Key
The application looks for the GROQ_API_KEY in your environment variables. Replace gsk_your_key_here with your actual key.
Windows (Command Prompt):
cmd
set GROQ_API_KEY=gsk_your_key_here
Use code with caution.

Linux / macOS:
bash
export GROQ_API_KEY=gsk_your_key_here
Use code with caution.

🚀 How to Run (Step-by-Step)
Navigate to Project Root
Open your terminal in the project folder:
bash
cd intelligent-form-agent
Use code with caution.

Launch the Orchestrator
Run the run.py file, which automatically triggers the Streamlit server:
bash
python src/run.py
Use code with caution.

Access the Agent
Open your browser and visit: http://localhost:8501

📺 Project Demonstration
Due to file size constraints, the demo video is hosted externally.
📽 Watch the Demo here:https://drive.google.com/file/d/1J6rkpziZbjxXUGUkkAIF9SbcGhSHqNgP/view?usp=sharing

📄 Example Queries & Expected Outputs
Standard Identity Forms
Action: Upload an Aadhaar PDF and click "Extract All Data".
Expected Output:
text
Aadhaar Number: 1234-5678-9012
Resident Name: John Doe
Gender: Male
DOB: 01/01/1990
Address: 123 Maple St, Delhi
Use code with caution.

Generic Forms (Hospital/Bank)

User Query	Expected Output
"Summarize this medical report"	A 3-to-4 point bulleted list summarizing key findings.
"What is the patient's blood pressure?"	Specific value (e.g., 120/80 mmHg) or "Information not found".
"Extract all information"	A clean list of every key-value pair detected in the document.

⚙️ Design Notes
Strict Mode Rules: The agent is hard-coded to reject hospital or bank forms when uploaded to the "Standard Identity" tab. This prevents data contamination and ensures the correct extraction logic is applied.
Zero Temperature: The LLM is configured with temperature=0. This ensures deterministic, factual responses and eliminates "hallucinations" or creative variations in data extraction.




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

## Environment Setup

### 1. Prerequisite
Ensure you have **Python 3.9+** installed and a **Groq API Key**.

1. Installation
Install the necessary dependencies using pip:
bash
pip install streamlit pymupdf groq
Use code with caution.

2. Configure API Key
The application requires a GROQ_API_KEY set in your environment variables. Replace gsk_your_key_here with your actual key.
Windows (Command Prompt):
dos
set GROQ_API_KEY=gsk_your_key_here
Use code with caution.

Linux / macOS:
bash
export GROQ_API_KEY=gsk_your_key_here
Use code with caution.

3. How to Run (Step-by-Step)
Navigate to Project Root: Open your terminal in the project folder.
bash
cd intelligent-form-agent
Use code with caution.

Launch the Orchestrator: Run the run.py file to automatically trigger the Streamlit server.
bash
python src/run.py
Use code with caution.

Access the Agent: Open your browser and visit: http://localhost:8501
4. Project Demonstration
Due to file size constraints, the demo video is hosted externally.
📽 Watch the demo here
5. Example Queries & Expected Outputs
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
Query: "Summarize this medical report"
Output: A 3-to-4 point summary list starting with dashes.
Query: "What is the patient's blood pressure?"
Output: The specific value from the document or "Information not found".
Query: "Extract all information"
Output: A clean list of every key-value pair found in the document.
6. Design Notes
Strict Mode Rules: The agent is instructed to reject hospital or bank forms in the "Standard" tab to prevent data contamination.
Zero Temperature: The LLM is set to temperature=0 to ensure high accuracy and consistent, factual responses.




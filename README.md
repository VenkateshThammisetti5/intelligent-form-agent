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

### 2. Install Dependencies
Install the required libraries for PDF processing, UI, and API communication:
```bash
pip install streamlit pymupdf groq
### 3. Configure API Key
The application looks for the `GROQ_API_KEY` in your environment variables:

**Windows (Command Prompt)**
```dos
set GROQ_API_KEY=gsk_your_key_here

### Linux / macOS
```bash
export GROQ_API_KEY=gsk_your_key_here


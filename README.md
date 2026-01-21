# Intelligent Form Agent

An **AI-powered document processing system** designed to handle both **standard identity documents** and **unstructured generic forms** using the **Groq LPU Inference Engine**.  
This agent provides **specialized extraction for Aadhaar forms** and **advanced analysis for other generic forms**.

---

## Overview

The **Intelligent Form Agent** acts as a **dual-mode gatekeeper and analyst** for PDF documents.

### Standard Identity Mode
- Uses **strict validation** to ensure only **Aadhaar documents** are processed
- Extracts specific identity fields such as:
  - Resident Name
  - Date of Birth (DOB)
  - Gender
  - Aadhaar Number
  - Address

### Generic Analysis Mode
- Processes **unstructured documents** such as hospital or bank forms
- Provides:
  - Summarization
  - Structured data extraction
  - Question answering (Q&A)
- Operates **strictly on the provided document context**

---

## Pipeline Architecture

The system operates through a **three-tier pipeline**:

### Ingestion (Streamlit & PyMuPDF)
- Users upload one or multiple PDF files
- The `fitz` (PyMuPDF) library extracts raw text from each page

### Reasoning (Groq & Llama-3.1)
- **Standard Gatekeeper**
  - Validates identity documents
  - Extracts a fixed set of identity fields
- **Generic Analyst**
  - Detects user intent:
    - Summary
    - Extraction
    - Q&A
  - Applies strict **anti-hallucination rules**

### Output (Streamlit UI)
- Identity form results are displayed **side-by-side**
- Generic analysis is rendered as **Markdown output**

---

## Environment Setup

### Prerequisites
- Python **3.9+**
- A valid **Groq API Key**

---

### Install Dependencies

```bash
pip install streamlit pymupdf groq

The application reads the API key from the environment variable GROQ_API_KEY.

Windows
set GROQ_API_KEY=gsk_your_key_here

Linux / macOS
export GROQ_API_KEY=gsk_your_key_here

How to Run (Step-by-Step)

Navigate to the project root directory:

cd intelligent-form-agent


Launch the orchestrator:

python src/run.py


Open your browser and access:

http://localhost:8501

Example Queries & Expected Outputs
Standard Identity Forms (Aadhaar)

Action:
Upload an Aadhaar PDF and click Extract All Data

Expected Output:

Aadhaar Number: 1234-5678-9012
Resident Name: John Doe
Gender: Male
DOB: 01/01/1990
Address: 123 Maple St, Delhi

Generic Forms (Hospital / Bank)

Query:

Summarize this medical report


Output:

3–4 point summary

Each line starts with -

Query:

What is the patient's blood pressure?


Output:

Specific value from the document

Or: Information not found

Query:

Extract all information


Output:

Clean list of all detected key-value pairs

Design Notes

Strict Mode Rules

Hospital and bank forms are rejected in Standard Identity Mode

Prevents data contamination

Zero Temperature

LLM temperature is set to 0

Ensures deterministic and accurate extraction

Prevents hallucinations in sensitive data

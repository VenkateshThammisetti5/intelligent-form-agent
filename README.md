
# Intelligent Form Agent



###### An AI-powered document processing system designed to handle both standard identity documents and unstructured generic forms using the Groq LPU Inference Engine. This agent provides specialized extraction for Aadhaar forms and advanced analysis for other generic forms.



#### Overview:



###### The Intelligent Form Agent acts as a dual-mode gatekeeper and analyst for PDF documents:

###### *Standard Identity Mode*: Uses strict validation to ensure only Aadhaar documents are processed, extracting specific fields like Resident            Name and DOB etc..

###### *Generic Analysis Mode*: Processes unstructured documents (like hospital or bank forms) to provide summaries, data extraction, and question-answering based strictly on the provided context.

#### 

#### Pipeline Architecture

###### 

###### The system operates through a structured three-tier pipeline:

###### Ingestion (Streamlit\&PyMuPDF): The user uploads one or multiple PDFs. The fitz (PyMuPDF) library extracts raw text from each page.

###### Reasoning (Groq \& Llama-3.1): \* Standard Gatekeeper: Validates identity documents and extracts a fixed set of fields.

###### Generic Analyst: Detects user intent (Summary, Extraction, or Q\&A) and applies strict anti-hallucination rules.

###### Output (Streamlit UI): Results are displayed side-by-side for identity forms or as markdown for generic analysis.



#### Environment Setup



###### 1\. Prerequisite

###### Ensure you have Python 3.9+ installed and a Groq API Key.

###### 

###### 2\. Install Dependencies

###### Install the required libraries for PDF processing, UI, and API communication:

###### 

###### Bash

###### pip install streamlit pymupdf groq



###### 3\. Configure API Key

###### The application looks for the GROQ\_API\_KEY in your environment variables:

###### 

###### DOS

###### \# Windows

###### set GROQ\_API\_KEY=gsk\_your\_key\_here

###### 

###### \# Linux/Mac

###### export GROQ\_API\_KEY=gsk\_your\_key\_here



### How to Run (Step-by-Step)

###### 

###### Navigate to Project Root: Open your terminal in the intelligent-form-agent folder.

###### Launch the Orchestrator: Run the run.py file, which automatically triggers the Streamlit server:

###### 

###### Bash

###### python src/run.py



###### Access the Agent: Open your browser to http://localhost:8501.

#### 

## Project Demonstration

Due to file size constraints, the project demonstration video is hosted on Google Drive.

🎥 **Watch the demo here:**  
[Google Drive – Project Demo](https://drive.google.com/file/d/1J6rkpziZbjxXUGUkkAIF9SbcGhSHqNgP/view?usp=sharing)


#### Example Queries \& Expected Outputs



###### *Standard Identity Forms:*



###### Action: Upload an Aadhaar PDF and click "Extract All Data".

###### 

###### Expected Output: ```text Aadhaar Number: 1234-5678-9012 Resident Name: John Doe Gender: Male DOB: 01/01/1990 Address: 123 Maple St, Delhi

###### 

###### 

###### *Generic Forms (Hospital/Bank)*



###### Query: "Summarize this medical report".

###### 

###### Output: A 3-to-4 point summary list starting with dashes.

###### 

###### Query: "What is the patient's blood pressure?".

###### 

###### Output: The specific value from the document or "Information not found".

###### 

###### Query: "Extract all information".

###### 

###### Output: A clean list of every key-value pair found in the document.

###### 

### Multi-Form Analysis (Holistic Insights)

**Action:** Upload multiple PDF documents together (e.g., multiple bank or hospital forms).

**Expected Output:**  
The agent analyzes all uploaded documents collectively to generate a combined summary or answer questions using information across all forms, strictly limited to the provided documents.


#### *Design Notes*



###### Strict Mode Rules: The agent is instructed to reject hospital or bank forms in the Standard tab to prevent data contamination.

###### 

###### Zero Temperature: The LLM is set to temperature=0 to ensure deterministic, accurate extraction and prevent hallucinations in sensitive data.

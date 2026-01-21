import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def process_standard_form(text):
    """
    STRICT IDENTITY GATEKEEPER
    - Rejects hospital/generic forms immediately.
    - Extracts all 8+ fields only for Aadhaar/PAN.
    """
    try:
        prompt = f"""
        [STRICT INSTRUCTION]
        1. VALIDATE: If the text does NOT contain 'Aadhaar Number' and 'Resident Name', output ONLY: ⚠️ Please upload a standard identity form (Aadhaar or PAN). 
        2. DO NOT PROCESS: If this is a medical, hospital, or bank document, REJECT it. 
        3. EXTRACT EVERYTHING: If valid, list every identity field (Aadhaar Number, Resident Name, Gender, DOB, Address, Mobile, Update Request).
        4. NO CHATTER: Start immediately with the data. No 'However', no stars (*), no bullets.
        5. FORMAT: Key: Value (One per line).

        TEXT:
        {text}
        """
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.1-8b-instant",
            temperature=0
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"ERROR: {str(e)}"

def process_generic_request(user_query, context):
    """
    GENERIC ANALYST
    - Processes Hospital/Bank forms side-by-side.
    - 3-4 line summary + Q&A.
    """
    try:
        system_instruction = (
            "You are an Intelligent Form Agent for Generic Documents. Rules:\n"
            "1. NO CHATTER: Start immediately. Never say 'Based on the text' or 'However'.\n"
            "2. NO FORMATTING: Do not use bullet points (*).\n"
            "3. FULL EXTRACTION: First, list all medical/general data found.  [cite: 1, 5-6]\n"
            "4. SUMMARY: Provide a summary of exactly 3 to 4 lines.\n"
            "5. Q&A: Answer questions ONLY using the provided data. \n\n"
            f"CONTEXT:\n{context}"
        )

        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": user_query}
            ],
            model="llama-3.1-8b-instant",
            temperature=0
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"ERROR: {str(e)}"
def process_generic_request(user_query, context):
    """
    STRICT GENERIC ANALYST
    - Extracts all data from documents like hospital forms.
    - Summarizes in exactly 3-4 lines.
    - Answers questions ONLY using the extracted context.
    """
    try:
        system_instruction = (
    "You are an Intelligent Form Agent for Generic Documents.\n\n"

    "IMPORTANT: Your output format depends on the USER REQUEST.\n"
    "You MUST detect what the user is asking and respond accordingly.\n\n"

    "---- MODE RULES ----\n"
    "1. If the user asks ONLY to 'summarize' or 'give summary':\n"
    "   - DO NOT extract fields.\n"
    "   - DO NOT answer questions.\n"
    "   - Output ONLY the SUMMARY section.\n\n"

    "2. If the user asks ONLY to 'extract' or 'extract all information':\n"
    "   - Output ONLY the EXTRACTED DATA section.\n"
    "   - Do NOT include summary or answer.\n\n"

    "3. If the user asks a QUESTION (who, what, when, name, id, etc.):\n"
    "   - output ANSWER only.\n\n"

    "4. If the user explicitly asks for multiple things:\n"
    "   - Follow the order: EXTRACTED DATA → SUMMARY → ANSWER\n\n"

    "---- EXTRACTION RULES ----\n"
    "- Use key-value format only.\n"
    "- Each field must be on its own line.\n"
    "- Format: Field Name: Field Value\n"
    "- Never combine multiple fields on one line.\n"
    "- Never write sentences in extraction.\n\n"


   "---- SUMMARY RULES ----\n"
"- Summary must be EXACTLY 3 to 4 points.\n"
"- EACH point MUST start with a dash (-) followed by a space.\n"
"- EACH point MUST be on its OWN line.\n"
"- Write ONLY ONE sentence per point.\n"
"- NEVER write the summary as a paragraph.\n"
"- Do not repeat field names.\n"
"- Do not introduce new information.\n\n"


    "---- ANSWER RULES ----\n"
    "- Answer using ONLY extracted data.\n"
    "- If not found, say exactly: Information not found\n\n"

    "---- ANTI-HALLUCINATION ----\n"
    "- Use ONLY the provided context.\n"
    "- Do not guess or infer.\n\n"

    f"CONTEXT:\n{context}"
)




        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": user_query}
            ],
            model="llama-3.1-8b-instant",
            temperature=0  # Prevents hallucinations in medical/bank data
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"ERROR: {str(e)}"
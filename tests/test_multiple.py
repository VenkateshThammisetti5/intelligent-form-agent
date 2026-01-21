from src.llm import process_document_request
import fitz
import os

def run_holistic_test():
    all_context = ""
    files = ["hospital_boxed_1.pdf", "hospital_boxed_2.pdf", "hospital_boxed_3.pdf"]
    
    # Combining all documents from data folder
    for i, file_name in enumerate(files):
        path = os.path.join("data", file_name)
        doc = fitz.open(path)
        text = "".join([p.get_text() for p in doc])
        all_text += f"\n[DOCUMENT {i+1}]:\n{text}\n"

    # Holistic Question
    query = "List all patient names and their respective ages from the uploaded forms."
    print("Testing Holistic Insight across 3 hospital forms...")
    
    result = process_document_request(query, all_text)
    print("\nHolistic Answer:\n", result)

if __name__ == "__main__":
    run_holistic_test()
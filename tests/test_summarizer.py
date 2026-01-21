from src.llm import process_document_request
import fitz

def run_summary_test():
    # Using Mohammed Irfan's record
    path = "data/hospital_boxed_3.pdf"
    
    doc = fitz.open(path)
    text = "".join([p.get_text() for p in doc])
    
    print(f"Generating 2-3 line summary for {path}...")
    # Keyword 'summarize' triggers the 2-3 line logic in llm.py
    summary = process_document_request("summarize", text)
    
    print("\nSummary Result:\n", summary)

if __name__ == "__main__":
    run_summary_test()
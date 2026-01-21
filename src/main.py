import streamlit as st
import fitz
from llm import process_standard_form, process_generic_request

st.set_page_config(layout="wide")
st.title("📄 Multi-Form Processing Agent")

# FIX: Define the tabs first so they can be referenced below
tab_std, tab_gen = st.tabs(["Standard[AADHAR] Forms", "Generic Forms"])

# --- TAB 1: STANDARD IDENTITY FORMS ---
with tab_std:
    st.header("Identity Extraction")
    uploaded_std = st.file_uploader("Upload Standard PDFs", type="pdf", accept_multiple_files=True, key="std_up")
    
    if st.button("Extract All Data", key="std_btn"):
        if uploaded_std:
            # Create side-by-side columns for multiple forms
            cols = st.columns(len(uploaded_std))
            
            for idx, file in enumerate(uploaded_std):
                with cols[idx]:
                    # Display Form Name as a header
                    st.markdown(f"**Form: {file.name}**")
                    st.divider()
                    
                    # Extract text from the PDF
                    doc = fitz.open(stream=file.read(), filetype="pdf")
                    text = "".join([page.get_text() for page in doc])
                    
                    # Call strict validator from llm.py [cite: 3-4]
                    result = process_standard_form(text)
                    
                    # Display clean data-only output
                    st.text(result)
        else:
            st.warning("Please upload at least one PDF file.")

# --- TAB 2: GENERIC DOCUMENT ANALYSIS ---
with tab_gen:
    st.header("Generic Form Analysis")
    st.info("Upload forms for summaries or Q&A based on extracted data.")
    
    uploaded_gen = st.file_uploader("Upload Generic PDFs", type="pdf", accept_multiple_files=True, key="gen_up")
    user_query = st.text_input("Ask a question (e.g., 'Summarize' or 'Who is the patient?')")
    
    if st.button("Send", key="gen_btn"):
        if uploaded_gen and user_query:
            # Combine text for holistic analysis
            combined_text = ""
            for i, file in enumerate(uploaded_gen):
                doc = fitz.open(stream=file.read(), filetype="pdf")
                combined_text += f"\n[DOC {i+1}]: " + "".join([page.get_text() for page in doc])
            
            with st.spinner("Analyzing..."):
                # Call generic logic (Extraction + 3-4 line summary + Q&A)  [cite: 1, 5-6]
                result = process_generic_request(user_query, combined_text)
                st.markdown(result)
        else:
            st.warning("Please upload files and enter a query.")
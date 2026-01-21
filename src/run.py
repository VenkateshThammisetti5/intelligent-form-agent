import os
import sys

# Ensure the app can find the src folder
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    # This triggers the Streamlit command automatically
    os.system("streamlit run src/main.py")
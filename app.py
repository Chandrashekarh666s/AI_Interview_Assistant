
import streamlit as st
from groq import Groq

# Page configuration
st.set_page_config(page_title="LLM", layout="centered")

# Application title
st.title("AI Interview Assistant")
st.caption("Practice and prepare for placements")

# Initialize Groq API client
try:
    client = Groq(
        api_key=st.secrets["GROQ_API_KEY"]
    )

except (KeyError, FileNotFoundError):
    st.error("API key is missing. Add it in Streamlit secrets.")
    st.stop()

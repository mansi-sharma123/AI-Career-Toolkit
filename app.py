import streamlit as st
from google import genai
import PyPDF2
import time

st.set_page_config(page_title="AI Career Toolkit", layout="wide")
st.title("AI Career Toolkit by Mansi Sharma")
st.write("LLM Powered Tools for Career Growth | College Project")
st.divider()

api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    client = genai.Client(api_key=api_key)
    uploaded = st.file_uploader("Upload Resume PDF", type="pdf")
    role = st.text_input("Dream Role", placeholder="e.g. SDE, Data Analyst")

    if st.button("Analyze"):
        if uploaded and role:
            reader = PyPDF2.PdfReader(uploaded)
            text = "".join([p.extract_text() or "" for p in reader.pages])
            prompt = f"Analyze this resume for {role} role. Give score out of 100, strengths, gaps, and suggestions: {text[:4000]}"

            with st.spinner("Analyzing..."):
                models_to_try = ["gemini-2.0-flash", "gemini-2.0-flash-lite", "gemini-1.5-flash", "gemini-flash-latest"]
                resp = None
                for m in models_to_try:
                    try:
                        resp = client.models.generate_content(model=m, contents=prompt)
                        break
                    except Exception as e:
                        time.sleep(1)
                        continue

                if resp:
                    st.success("Analysis Complete!")
                    st.write(resp.text)
                else:
                    st.error("Google server busy hai (503). 30 sec baad retry karo.")
        else:
            st.warning("Please upload resume and enter role")
else:
    st.warning("Sidebar me API Key dalo - tab tool dikhega")

# LLM-Apps
Welcome to the GenAI &amp; LLM App Development Series – 150 Real AI Tools for Projects.

https://www.youtube.com/playlist?list=PLp4WMXO7ORJE57QOVsybKKiqDGI739EvB
=======
# 🚀 AI-Career-Toolkit
### By Mansi Sharma | LLM Apps - College Project

> LLM Powered Tools for Career Growth - Resume Analysis, Gap Detection & Career Guidance

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B.svg)](https://streamlit.io)
[![Gemini](https://img.shields.io/badge/Powered%20by-Gemini%201.5%20Flash-8E75B2.svg)](https://ai.google.dev)

🔴 **Live Demo:** Coming Soon on Streamlit Cloud
📹 **Demo Video:** (Add your Loom/YouTube link here)

---

## 📌 About The Project
Students often don't know where their resume stands. This toolkit uses **Google Gemini LLM** to give an instant, honest evaluation of your resume for your dream role.

This project was built to solve the **Gemini 503 Model Overloaded** issue faced by many students by implementing a smart **auto-fallback system**.

## ✨ Key Features
- 📊 **Resume Score** - Get a score like **68/100** with detailed breakdown
- 💪 **Strength Analysis** - Highlights your top skills and achievements  
- 🎯 **Skill Gap Finder** - Tells you exactly what's missing for SDE / Data Analyst roles
- 🔄 **Auto-Fallback** - If `gemini-1.5-flash` is busy (503), it auto-switches to `gemini-2.0-flash`
- 📄 **PDF Support** - Direct PDF upload with PyPDF2 parsing

## 🛠️ Tech Stack
- **Frontend:** Streamlit
- **LLM:** Google GenAI - Gemini 1.5 Flash, Gemini 2.0 Flash
- **PDF Processing:** PyPDF2
- **Language:** Python

## 🚀 How to Run Locally

** Clone the repo**
```bash
git clone https://github.com/mansi-sharma123/AI-Career-Toolkit.git
cd AI-Career-Toolkit
```

``` pip install -r requirements.txt ```

``` streamlit run app.py ```

** Enter your Gemini API Key in the sidebar and start analyzing! **

## 🎬 Demo Flow
1. Get free API key from aistudio.google.com
2. Upload your Resume PDF
3. Enter Dream Role - e.g., SDE
4. Click Analyze

## 🧠 Challenges
- Fixed Gemini 503 error with auto-fallback logic

## 🔮 Future Scope
- Cover Letter Generator
- LinkedIn Optimizer
- Interview Questions

## 👩‍💻 Author
Mansi Sharma | @mansi-sharma123 | College Project 2026

---
Star this repo ⭐
>>>>>>> 3bad79f46b0adcd2cbebe9cf814e32651cefdbef

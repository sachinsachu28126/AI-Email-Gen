import google.generativeai as genai
import streamlit as st

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_email(email_type, tone, user_input):
    prompt = f"""
You are a world-class corporate communication assistant.

Write a professional email.

Type: {email_type}
Tone: {tone}
User Input: {user_input}

FORMAT:
Subject:
Greeting:
Body:
Closing:

RULES:
- Human-like writing
- Perfect grammar
- Corporate standard email
"""

    return model.generate_content(prompt).text
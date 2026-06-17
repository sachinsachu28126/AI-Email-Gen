import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_email(email_type, user_input):
    prompt = f"""
You are a professional email writer.

Write a formal email with:
- Subject
- Greeting
- Body
- Closing

Email Type: {email_type}
User Input: {user_input}

Rules:
- Professional tone
- Clear and concise
"""

    response = model.generate_content(prompt)
    return response.text
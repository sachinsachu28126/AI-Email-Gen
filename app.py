import streamlit as st
from auth import login, is_logged_in
from email_engine import generate_email
from db import save_email, get_user_emails
from pdf_export import create_pdf

st.set_page_config(page_title="AI Email Enterprise", layout="wide")

# LOGIN
login()

if not is_logged_in():
    st.warning("Please login to continue")
    st.stop()

user = st.session_state["user"]

st.title("📧 AI Email Enterprise System")

# SIDEBAR HISTORY
st.sidebar.title("📜 Your Emails")
emails = get_user_emails(user)

for e in emails[:10]:
    st.sidebar.write(f"📌 {e[2]}")

# INPUTS
email_type = st.selectbox(
    "Email Type",
    ["Leave Request", "Job Application", "Complaint", "Follow-up"]
)

tone = st.selectbox(
    "Tone",
    ["Formal", "Polite", "Urgent", "Friendly"]
)

user_input = st.text_area("Enter details")

# SESSION STORAGE
if "email" not in st.session_state:
    st.session_state.email = ""

# GENERATE
if st.button("🚀 Generate Email"):

    email = generate_email(email_type, tone, user_input)
    st.session_state.email = email

    st.success("Generated Successfully")

    st.text_area("Output", email, height=300)

    save_email(user, email_type, email)

# DOWNLOADS
if st.session_state.email:

    st.download_button(
        "📥 Download TXT",
        st.session_state.email,
        file_name="email.txt"
    )

    pdf_file = create_pdf(st.session_state.email)

    with open(pdf_file, "rb") as f:
        st.download_button(
            "📄 Download PDF",
            f,
            file_name="email.pdf"
        )
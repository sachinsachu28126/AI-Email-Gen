import streamlit as st
from email_generator import generate_email
from history import save_email, get_history

st.set_page_config(page_title="AI Email Generator", page_icon="📧", layout="wide")

st.title("📧 AI Email Generator")

# Sidebar history
st.sidebar.header("📜 History")
history = get_history()

if history:
    for item in history[:10]:
        st.sidebar.write(f"📌 {item[1]}")
else:
    st.sidebar.write("No history yet")

# Input UI
email_type = st.selectbox(
    "Select Email Type",
    ["Leave Request", "Job Application", "Complaint", "Follow-up"]
)

user_input = st.text_area("Enter details (optional)")

# Generate button
if st.button("🚀 Generate Email"):

    if not user_input:
        user_input = "No details provided"

    with st.spinner("Generating email..."):
        result = generate_email(email_type, user_input)

    st.success("Email Generated!")

    st.subheader("📧 Output")
    st.text_area("", result, height=300)

    st.download_button("📥 Download Email", result)

    save_email(email_type, result)
import streamlit as st
import google.generativeai as genai
import os

# 1. Page Configuration
st.set_page_config(page_title="Blood Donation AI", layout="centered")
st.title("🩸 BloodSync & AI Emergency Parser")

# 2. Get AI API Key from Environment Variables safely
api_key = os.environ.get("GEMINI_API_KEY", "")

# 3. Core Feature: Live Dashboard of requests (Simulated Database)
if "requests" not in st.session_state:
    st.session_state.requests = [
        {"type": "O-", "location": "City General Hospital", "urgency": "CRITICAL"},
        {"type": "A+", "location": "Red Cross Center", "urgency": "MEDIUM"}
    ]

st.subheader("📋 Active Emergency Blood Requests")
for req in st.session_state.requests:
    st.warning(f"🩸 Type: {req['type']} | 📍 Location: {req['location']} | 🚨 Priority: {req['urgency']}")

# 4. Required AI Feature: Parse unstructured text into structured fields
st.subheader("🤖 AI Urgent Request Assistant")
st.write("Paste a messy text message from social media to instantly extract details.")

user_input = st.text_area("Example: My cousin needs B+ blood at Mercy Hospital urgently!!")

if st.button("Parse with AI"):
    if not api_key:
        st.error("AI API Key missing. Please configure GEMINI_API_KEY in your deployment environment variables.")
    elif user_input:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-2.5-flash')
            
            # YOUR CUSTOM SYSTEM PROMPT REQUIRED BY THE RUBRIC
            system_prompt = (
                "You are an urgent medical logistics assistant. Read the user's raw message "
                "about a blood request. Extract the Blood Type, Hospital/Location, and "
                "categorize the urgency strictly as LOW, MEDIUM, or CRITICAL. "
                "Format your final output clearly as a bulleted list."
            )
            
            response = model.generate_content(f"{system_prompt}\n\nUser Message: {user_input}")
            st.success("AI Analysis Complete:")
            st.write(response.text)
            
        except Exception as e:
            st.error(f"Error connecting to AI: {e}")

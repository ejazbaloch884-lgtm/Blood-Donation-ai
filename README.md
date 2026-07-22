# 🩸 BloodSync & AI Emergency Parser

### [🔗 Click Here to Open the Live Deployed App](https://streamlit.app)

## 1. The Problem & Idea
Finding specific blood types during sudden medical emergencies is chaotic and relies heavily on unorganized social media posts. This app centralizes requests and uses AI to instantly process messy text descriptions into structured medical alerts.

## 2. Full Features List
* **Real-time Request Board**: View active donor needs sorted by location and priority level.
* **AI Emergency Parser**: Instantly converts raw user descriptions into structured data fields.

## 3. The AI Feature & System Instructions
The AI feature takes messy text inputs and classifies urgency levels. 
**System Prompt Used:**
> "You are an urgent medical logistics assistant. Read the user's raw message about a blood request. Extract the Blood Type, Hospital/Location, and categorize the urgency strictly as LOW, MEDIUM, or CRITICAL. Format your final output clearly as a bulleted list."

## 4. Tech Stack & Models Used
* **Frontend/Backend UI**: Streamlit (Python)
* **Hosting Platform**: Streamlit Community Cloud
* **AI Model**: Google Gemini 1.5 Flash

## 5. How to Run Locally
1. Clone the repo: `git clone https://github.com`
2. Install packages: `pip install -r requirements.txt`
3. Set your local environment variable for `GEMINI_API_KEY`.
4. Run locally: `streamlit run app.py`

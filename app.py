import datetime as dt
import streamlit as st

from Tools import load_visa_matrix, check_visa, get_weather_forecast
from llm_client import RemoteMistralLLM, build_travel_report

st.set_page_config(page_title="Travel Assistant", page_icon="🧳")
st.title("🧳 Travel Assistant")

# ---- sidebar: connection to the Kaggle backend --------------------------
with st.sidebar:
    st.subheader("Backend connection")
    api_url = st.text_input("Ngrok URL", value="https://your-ngrok-url.ngrok-free.dev/generate")
    api_key = st.text_input("API key", value="secret123", type="password")

CSV_PATH = "passport-index-matrix.csv"  


@st.cache_data
def get_matrix():
    return load_visa_matrix(CSV_PATH)


df = get_matrix()
countries = sorted(set(df.index) | set(df.columns))

col1, col2 = st.columns(2)
with col1:
    departure = st.selectbox("Departure country", countries)
with col2:
    destination = st.selectbox("Destination country", [c for c in countries if c != departure])

start_date = st.date_input("Arrival date", value=dt.date.today() + dt.timedelta(days=14))
num_days = st.number_input("Trip length (days)", min_value=1, max_value=30, value=5)
end_date = start_date + dt.timedelta(days=int(num_days))

if st.button("Generate travel report"):
    if not api_url or "your-ngrok-url" in api_url:
        st.error("Set a valid ngrok URL in the sidebar first.")
        st.stop()

    with st.spinner("Checking visa requirements..."):
        visa_info = check_visa(df, departure, destination)
    st.subheader("🛂 Visa status")
    st.write(visa_info["message"])

    with st.spinner("Fetching weather forecast..."):
        try:
            weather = get_weather_forecast(
                destination, start_date.isoformat(), end_date.isoformat()
            )
        except Exception as e:
            weather = None
            st.warning(f"Weather forecast unavailable: {e}")

    llm = RemoteMistralLLM(api_url=api_url, api_key=api_key)

    with st.spinner("Generating travel plan and checklist..."):
        report = build_travel_report(
            llm=llm,
            departure=departure,
            destination=destination,
            num_days=int(num_days),
            visa_info=visa_info,
            weather=weather,
        )

    st.subheader("📅 Day-by-day plan")
    st.write(report["plan"])

    st.subheader("🎒 What to prepare / bring")
    st.write(report["checklist"])
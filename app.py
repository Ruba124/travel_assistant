# import datetime as dt
# import streamlit as st

# from Tools import load_visa_matrix, check_visa, get_weather_forecast
# from llm_client import RemoteMistralLLM, build_travel_report

# st.set_page_config(page_title="Travel Assistant", page_icon="🧳")
# st.title("🧳 Travel Assistant")

# # ---- sidebar: connection to the Kaggle backend --------------------------
# with st.sidebar:
#     st.subheader("Backend connection")
#     api_url = st.text_input("Ngrok URL", value="https://your-ngrok-url.ngrok-free.dev/generate")
#     api_key = st.text_input("API key", value="secret123", type="password")

# CSV_PATH = "passport-index-matrix.csv"  


# @st.cache_data
# def get_matrix():
#     return load_visa_matrix(CSV_PATH)


# df = get_matrix()
# countries = sorted(set(df.index) | set(df.columns))

# col1, col2 = st.columns(2)
# with col1:
#     departure = st.selectbox("Departure country", countries)
# with col2:
#     destination = st.selectbox("Destination country", [c for c in countries if c != departure])

# start_date = st.date_input("Arrival date", value=dt.date.today() + dt.timedelta(days=14))
# num_days = st.number_input("Trip length (days)", min_value=1, max_value=30, value=5)
# end_date = start_date + dt.timedelta(days=int(num_days))

# if st.button("Generate travel report"):
#     if not api_url or "your-ngrok-url" in api_url:
#         st.error("Set a valid ngrok URL in the sidebar first.")
#         st.stop()

#     with st.spinner("Checking visa requirements..."):
#         visa_info = check_visa(df, departure, destination)
#     st.subheader("🛂 Visa status")
#     st.write(visa_info["message"])

#     with st.spinner("Fetching weather forecast..."):
#         try:
#             weather = get_weather_forecast(
#                 destination, start_date.isoformat(), end_date.isoformat()
#             )
#         except Exception as e:
#             weather = None
#             st.warning(f"Weather forecast unavailable: {e}")

#     llm = RemoteMistralLLM(api_url=api_url, api_key=api_key)

#     with st.spinner("Generating travel plan and checklist..."):
#         report = build_travel_report(
#             llm=llm,
#             departure=departure,
#             destination=destination,
#             num_days=int(num_days),
#             visa_info=visa_info,
#             weather=weather,
#         )

#     st.subheader("📅 Day-by-day plan")
#     st.write(report["plan"])

#     st.subheader("🎒 What to prepare / bring")
#     st.write(report["checklist"])
# 
# import datetime as dt
# import streamlit as st

# from Tools import load_visa_matrix, check_visa, get_weather_forecast
# from llm_client import RemoteMistralLLM, build_travel_report

# st.set_page_config(page_title="Travel Assistant", page_icon="🧳")
# st.title("🧳 Travel Assistant")

# # ---- sidebar: connection to the Kaggle backend --------------------------
# with st.sidebar:
#     st.subheader("Backend connection")
#     api_url = st.text_input("Ngrok URL", value="https://joyride-duty-hurler.ngrok-free.dev/generate")
#     api_key = st.text_input("API key", value="secret123", type="password")

# CSV_PATH = "passport-index-matrix.csv"  # place your CSV next to this file


# @st.cache_data
# def get_matrix():
#     return load_visa_matrix(CSV_PATH)


# df = get_matrix()
# countries = sorted(set(df.index) | set(df.columns))

# col1, col2 = st.columns(2)
# with col1:
#     departure = st.selectbox("Departure country", countries)
# with col2:
#     destination = st.selectbox("Destination country", [c for c in countries if c != departure])

# start_date = st.date_input("Arrival date", value=dt.date.today() + dt.timedelta(days=14))
# num_days = st.number_input("Trip length (days)", min_value=1, max_value=30, value=5)
# end_date = start_date + dt.timedelta(days=int(num_days))

# if st.button("Generate travel report"):
#     if not api_url or "your-ngrok-url" in api_url:
#         st.error("Set a valid ngrok URL in the sidebar first.")
#         st.stop()

#     with st.spinner("Checking visa requirements..."):
#         visa_info = check_visa(df, departure, destination)
#     st.subheader("🛂 Visa status")
#     st.write(visa_info["message"])

#     with st.spinner("Fetching weather forecast..."):
#         try:
#             weather = get_weather_forecast(
#                 destination, start_date.isoformat(), end_date.isoformat()
#             )
#         except Exception as e:
#             weather = None
#             st.warning(f"Weather forecast unavailable: {e}")
#         else:
#             if weather and weather.get("source") == "historical_estimate":
#                 st.info(
#                     "Trip is too far out for a live forecast — showing last year's "
#                     "weather on the same dates as an estimate."
#                 )

#     llm = RemoteMistralLLM(api_url=api_url, api_key=api_key)

#     with st.spinner("Generating travel plan and checklist..."):
#         report = build_travel_report(
#             llm=llm,
#             departure=departure,
#             destination=destination,
#             num_days=int(num_days),
#             visa_info=visa_info,
#             weather=weather,
#         )

#     st.subheader("📅 Day-by-day plan")
#     st.write(report["plan"])

#     st.subheader("🎒 What to prepare / bring")
#     st.write(report["checklist"])
# import datetime as dt
# import streamlit as st

# from Tools import load_visa_matrix, check_visa, get_weather_forecast
# from llm_client import RemoteMistralLLM, build_travel_report

# st.set_page_config(page_title="Travel Assistant", page_icon="🧳")
# st.title("🧳 Travel Assistant")

# # ---- sidebar: connection to the Kaggle backend --------------------------
# with st.sidebar:
#     st.subheader("Backend connection")
#     api_url = st.text_input("Ngrok URL", value="https://joyride-duty-hurler.ngrok-free.dev/generate")
#     api_key = st.text_input("API key", value="secret123", type="password")

# CSV_PATH = "passport-index-matrix.csv"  # place your CSV next to this file


# @st.cache_data
# def get_matrix():
#     return load_visa_matrix(CSV_PATH)


# df = get_matrix()
# countries = sorted(set(df.index) | set(df.columns))

# col1, col2 = st.columns(2)
# with col1:
#     departure = st.selectbox("Departure country", countries)
# with col2:
#     destination = st.selectbox("Destination country", [c for c in countries if c != departure])

# start_date = st.date_input("Arrival date", value=dt.date.today() + dt.timedelta(days=14))
# num_days = st.number_input("Trip length (days)", min_value=1, max_value=30, value=5)
# end_date = start_date + dt.timedelta(days=int(num_days))

# if st.button("Generate travel report"):
#     if not api_url or "your-ngrok-url" in api_url:
#         st.error("Set a valid ngrok URL in the sidebar first.")
#         st.stop()

#     with st.spinner("Checking visa requirements..."):
#         visa_info = check_visa(df, departure, destination)
#     st.subheader("🛂 Visa status")
#     st.write(visa_info["message"])

#     with st.spinner("Fetching weather forecast..."):
#         try:
#             weather = get_weather_forecast(
#                 destination, start_date.isoformat(), end_date.isoformat()
#             )
#         except Exception as e:
#             weather = None
#             st.warning(f"Weather forecast unavailable: {e}")
#         else:
#             if weather and weather.get("source") == "historical_estimate":
#                 st.info(
#                     "Trip is too far out for a live forecast — showing last year's "
#                     "weather on the same dates as an estimate."
#                 )

#     llm = RemoteMistralLLM(api_url=api_url, api_key=api_key)

#     with st.spinner("Generating travel plan and checklist..."):
#         report = build_travel_report(
#             llm=llm,
#             departure=departure,
#             destination=destination,
#             num_days=int(num_days),
#             visa_info=visa_info,
#             weather=weather,
#         )

#     st.subheader("📅 Day-by-day plan")
#     st.write(report["plan"] or "_The model returned an empty response for this step — try regenerating._")

#     st.subheader("🎒 What to prepare / bring")
#     st.write(report["checklist"] or "_The model returned an empty response for this step — try regenerating._")
# import datetime as dt
# import streamlit as st
 
# from Tools import load_visa_matrix, check_visa, get_weather_forecast
# from llm_client import RemoteMistralLLM, build_travel_report, summarize_weather
 
# st.set_page_config(page_title="Travel Assistant", page_icon="🧳")
# st.title("🧳 Travel Assistant")
 
# # ---- sidebar: connection to the Kaggle backend --------------------------
# with st.sidebar:
#     st.subheader("Backend connection")
#     api_url = st.text_input("Ngrok URL", value="https://joyride-duty-hurler.ngrok-free.dev/generate")
#     api_key = st.text_input("API key", value="secret123", type="password")
 
# CSV_PATH = "passport-index-matrix.csv"  # place your CSV next to this file
 
 
# @st.cache_data
# def get_matrix():
#     return load_visa_matrix(CSV_PATH)
 
 
# df = get_matrix()
# countries = sorted(set(df.index) | set(df.columns))
 
# col1, col2 = st.columns(2)
# with col1:
#     departure = st.selectbox("Departure country", countries)
# with col2:
#     destination = st.selectbox("Destination country", [c for c in countries if c != departure])
 
# start_date = st.date_input("Arrival date", value=dt.date.today() + dt.timedelta(days=14))
# num_days = st.number_input("Trip length (days)", min_value=1, max_value=30, value=5)
# end_date = start_date + dt.timedelta(days=int(num_days))
 
# if st.button("Generate travel report"):
#     if not api_url or "your-ngrok-url" in api_url:
#         st.error("Set a valid ngrok URL in the sidebar first.")
#         st.stop()
 
#     with st.spinner("Checking visa requirements..."):
#         visa_info = check_visa(df, departure, destination)
#     st.subheader("🛂 Visa status")
#     st.write(visa_info["message"])
 
#     with st.spinner("Fetching weather forecast..."):
#         try:
#             weather = get_weather_forecast(
#                 destination, start_date.isoformat(), end_date.isoformat()
#             )
#         except Exception as e:
#             weather = None
#             st.warning(f"Weather forecast unavailable: {e}")
 
#     st.subheader("🌤️ Weather")
#     if weather and weather.get("source") == "historical_estimate":
#         st.caption("Trip is too far out for a live forecast — showing last year's weather on the same dates as an estimate.")
#     st.write(summarize_weather(weather))
 
#     llm = RemoteMistralLLM(api_url=api_url, api_key=api_key)
 
#     with st.spinner("Generating travel plan and checklist..."):
#         report = build_travel_report(
#             llm=llm,
#             departure=departure,
#             destination=destination,
#             num_days=int(num_days),
#             visa_info=visa_info,
#             weather=weather,
#         )
 
#     st.subheader("📅 Day-by-day plan")
#     st.write(report["plan"] or "_The model returned an empty response for this step — try regenerating._")
 
#     st.subheader("🎒 What to prepare / bring")
#     st.write(report["checklist"] or "_The model returned an empty response for this step — try regenerating._")
import datetime as dt
import streamlit as st
import base64
 
from Tools import load_visa_matrix, check_visa, get_weather_forecast
from llm_client import RemoteMistralLLM, build_travel_report, summarize_weather
 
# 1. Page config MUST be the first Streamlit command
st.set_page_config(page_title="Travel Assistant", page_icon="🧳", layout="centered")
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
img_base64 = get_base64_image("OIP.webp")
# 2. Modern UI Custom CSS
# -> Change the 'background-image' URL to your own image
# -> Change 'filter: blur(8px);' to increase or decrease the blur
# page_bg_css = """
# <style>
# /* Background Image with Blur */
# .stApp::before {
#     content: "";
#     position: fixed;
#     top: 0;
#     left: 0;
#     width: 100vw;
#     height: 100vh;
#     background-image: url("data:image/webp;base64,{img_base64}"); 
#     background-position: center;
#     background-repeat: no-repeat;
#     filter: blur(8px); /* <-- CONTROLS THE BLUR AMOUNT */
#     z-index: -1;
# }

# /* Glassmorphism container for readability */
# .block-container {
#     background-color: rgba(255, 255, 255, 0.85); /* Semi-transparent white */
#     border-radius: 16px;
#     padding: 2.5rem !important;
#     box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
#     backdrop-filter: blur(4px);
#     border: 1px solid rgba(255, 255, 255, 0.18);
#     margin-top: 2rem;
#     margin-bottom: 2rem;
# }

# /* Modern Gradient Button */
# div.stButton > button {
#     background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 100%);
#     color: white;
#     border: none;
#     border-radius: 8px;
#     padding: 0.5rem 1rem;
#     font-weight: 600;
#     transition: all 0.3s ease;
#     width: 100%;
# }
# div.stButton > button:hover {
#     transform: translateY(-2px);
#     box-shadow: 0 4px 12px rgba(124, 58, 237, 0.4);
#     color: white;
#     border: none;
# }

# /* Softer borders for inputs */
# .stTextInput>div>div>input, 
# .stSelectbox>div>div>div, 
# .stNumberInput>div>div>input, 
# .stDateInput>div>div>input {
#     border-radius: 8px;
#     border: 1px solid #CBD5E1;
# }
# .stTextInput>div>div>input:focus, 
# .stSelectbox>div>div>div:focus {
#     border-color: #4F46E5;
#     box-shadow: 0 0 0 1px #4F46E5;
# }

# /* Ensure text stays dark on the light glass background */
# h1, h2, h3, p, .stMarkdown {
#     color: #1E293B !important; 
# }
# </style>
# """
page_bg_css = f"""
<style>
/* 1. Make the default Streamlit backgrounds transparent */
[data-testid="stAppViewContainer"], [data-testid="stHeader"] {{
    background-color: transparent !important;
}}

/* 2. Set the blurred background image */
[data-testid="stAppViewContainer"]::before {{
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-image: url("data:image/webp;base64,{img_base64}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    filter: blur(8px); /* Adjust blur here */
    z-index: -1;
}}

/* 3. Glassmorphism card container (so text is readable) */
.block-container {{
    background-color: rgba(255, 255, 255, 0.85);
    border-radius: 16px;
    padding: 2.5rem !important;
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
    backdrop-filter: blur(4px);
    border: 1px solid rgba(255, 255, 255, 0.18);
    margin-top: 2rem;
    margin-bottom: 2rem;
}}

/* 4. Modern Gradient Button */
div.stButton > button {{
    background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 100%);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 0.5rem 1rem;
    font-weight: 600;
    transition: all 0.3s ease;
    width: 100%;
}}
div.stButton > button:hover {{
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(124, 58, 237, 0.4);
    color: white;
    border: none;
}}

/* 5. Input styling */
.stTextInput>div>div>input, 
.stSelectbox>div>div>div, 
.stNumberInput>div>div>input, 
.stDateInput>div>div>input {{
    border-radius: 8px;
    border: 1px solid #CBD5E1;
}}
.stTextInput>div>div>input:focus, 
.stSelectbox>div>div>div:focus {{
    border-color: #4F46E5;
    box-shadow: 0 0 0 1px #4F46E5;
}}

/* 6. Dark text for legibility */
h1, h2, h3, p, .stMarkdown {{
    color: #1E293B !important; 
}}
</style>
"""

st.markdown(page_bg_css, unsafe_allow_html=True)

st.title("🧳 Travel Assistant")
 
# ---- sidebar: connection to the Kaggle backend --------------------------
with st.sidebar:
    st.subheader("Backend connection")
    api_url = st.text_input("Ngrok URL", value="https://joyride-duty-hurler.ngrok-free.dev/generate")
    api_key = st.text_input("API key", value="secret123", type="password")
 
CSV_PATH = "passport-index-matrix.csv"  # place your CSV next to this file
 
 
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
 
    st.subheader("🌤️ Weather")
    if weather and weather.get("source") == "historical_estimate":
        st.caption("Trip is too far out for a live forecast — showing last year's weather on the same dates as an estimate.")
    st.write(summarize_weather(weather))
 
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
    st.write(report["plan"] or "_The model returned an empty response for this step — try regenerating._")
 
    st.subheader("🎒 What to prepare / bring")
    st.write(report["checklist"] or "_The model returned an empty response for this step — try regenerating._")
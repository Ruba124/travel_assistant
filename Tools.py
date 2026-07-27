"""
Local tools used by the LangChain controller — no GPU call involved.
"""

from typing import Dict, Optional
import pandas as pd
import requests

# ---- Visa tool --------------------------------------------------------------

VISA_LABELS = {
    "visa free": "Visa-free entry (no fixed duration in the data — e.g. freedom of "
                 "movement, tourist registration, e-ticket, or arrival-card countries).",
    "visa on arrival": "Visa on arrival — effectively visa-free.",
    "eta": "Electronic Travel Authorisation (ETA/ESTA/eVisitor) required before travel.",
    "e-visa": "Electronic visa (e-Visa) required before travel.",
    "visa required": "A standard visa is required before travel.",
    "no admission": "Entry is not permitted (active travel ban or restricted destination).",
}


def load_visa_matrix(csv_path: str) -> pd.DataFrame:
    """CSV layout: first column ('Passport') = departure/passport country (row index),
    remaining column headers = destination countries."""
    return pd.read_csv(csv_path, index_col=0)


def check_visa(df: pd.DataFrame, departure: str, destination: str) -> Dict:
    if departure not in df.index:
        raise ValueError(f"Departure country '{departure}' not found in CSV rows")
    if destination not in df.columns:
        raise ValueError(f"Destination country '{destination}' not found in CSV columns")

    raw = df.loc[departure, destination]
    raw_str = str(raw).strip().lower()

    if raw_str == "-1":
        return {
            "status": "same_country",
            "days": None,
            "message": "Departure and destination are the same country — no visa needed.",
        }
    if raw_str.replace(".", "", 1).isdigit():
        days = int(float(raw_str))
        return {
            "status": "visa_free",
            "days": days,
            "message": f"Visa-free for up to {days} days.",
        }
    if raw_str in VISA_LABELS:
        return {
            "status": raw_str.replace(" ", "_"),
            "days": None,
            "message": VISA_LABELS[raw_str],
        }
    return {"status": "unknown", "days": None, "message": f"Unrecognized CSV value: {raw}"}


# ---- Weather tool -------------------------------------------------------------
# Uses Open-Meteo (no API key required). Note: the free forecast endpoint only
# covers roughly the next 16 days — for trips further out, treat this as
# indicative rather than precise, or swap in a climate-normals API.

def get_coordinates(place_name: str):
    resp = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": place_name, "count": 1},
        timeout=15,
    )
    resp.raise_for_status()
    results = resp.json().get("results")
    if not results:
        raise ValueError(f"Could not geocode '{place_name}'")
    r = results[0]
    return r["latitude"], r["longitude"]


def get_weather_forecast(place_name: str, start_date: str, end_date: str) -> Optional[Dict]:
    lat, lon = get_coordinates(place_name)
    resp = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": lat,
            "longitude": lon,
            "daily": "temperature_2m_max,temperature_2m_min,precipitation_probability_max",
            "timezone": "auto",
            "start_date": start_date,
            "end_date": end_date,
        },
        timeout=15,
    )
    resp.raise_for_status()
    return resp.json()
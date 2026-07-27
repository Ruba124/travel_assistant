from typing import Optional, List, Dict, Any
import requests

try:
    from langchain_core.language_models.llms import LLM
except ImportError:  # older langchain versions
    from langchain.llms.base import LLM


class RemoteMistralLLM(LLM):
    """LangChain-compatible wrapper around the FastAPI/ngrok endpoint on Kaggle."""

    api_url: str
    api_key: str
    max_length: int = 400
    timeout: int = 120

    @property
    def _llm_type(self) -> str:
        return "remote_mistral_nemo"

    def _call(self, prompt: str, stop: Optional[List[str]] = None, **kwargs: Any) -> str:
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {"prompt": prompt, "max_length": self.max_length}
        resp = requests.post(self.api_url, headers=headers, json=payload, timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()["response"]


def _summarize_weather(weather: Optional[Dict]) -> str:
    if not weather or "daily" not in weather:
        return "Weather data unavailable — assume moderate conditions and pack for variability."
    daily = weather["daily"]
    highs = daily.get("temperature_2m_max", [])
    lows = daily.get("temperature_2m_min", [])
    rain = daily.get("precipitation_probability_max", [])
    if not highs:
        return "Weather data unavailable."
    avg_high = sum(highs) / len(highs)
    avg_low = sum(lows) / len(lows)
    avg_rain = sum(rain) / len(rain) if rain else 0
    return (
        f"Average high {avg_high:.0f}°C, average low {avg_low:.0f}°C, "
        f"average chance of rain {avg_rain:.0f}%."
    )


def build_travel_report(
    llm: RemoteMistralLLM,
    departure: str,
    destination: str,
    num_days: int,
    visa_info: Dict,
    weather: Optional[Dict],
) -> Dict[str, str]:
    """Two-step prompt chain: day-by-day plan first, then a prep checklist
    that reuses the plan's output as context (chaining keywords forward)."""

    weather_summary = _summarize_weather(weather)

    plan_prompt = (
        f"You are a travel assistant. Create a {num_days}-day itinerary for a trip "
        f"from {departure} to {destination}.\n"
        f"Visa situation: {visa_info['message']}\n"
        f"Weather during the trip: {weather_summary}\n"
        f"Give a concise day-by-day plan (activities, pacing, any weather-related "
        f"adjustments). Keep it practical."
    )
    plan = llm(plan_prompt).strip()

    checklist_prompt = (
        f"Based on this itinerary for a trip from {departure} to {destination}:\n"
        f"{plan}\n\n"
        f"Visa situation: {visa_info['message']}\n"
        f"Weather: {weather_summary}\n\n"
        f"List what the traveller should prepare before departure: required "
        f"documents (visa/ETA if applicable), suggested clothing/gear given the "
        f"weather, and other practical tips (currency, adapters, tickets, etc). "
        f"Keep it as a short checklist."
    )
    checklist = llm(checklist_prompt).strip()

    return {"plan": plan, "checklist": checklist}

# from typing import Optional, List, Dict, Any
# import requests

# try:
#     from langchain_core.language_models.llms import LLM
# except ImportError:  # older langchain versions
#     from langchain.llms.base import LLM


# class RemoteMistralLLM(LLM):
#     """LangChain-compatible wrapper around the FastAPI/ngrok endpoint on Kaggle."""

#     api_url: str
#     api_key: str
#     max_length: int = 400
#     timeout: int = 120

#     @property
#     def _llm_type(self) -> str:
#         return "remote_mistral_nemo"

#     def _call(self, prompt: str, stop: Optional[List[str]] = None, **kwargs: Any) -> str:
#         headers = {"Authorization": f"Bearer {self.api_key}"}
#         payload = {"prompt": prompt, "max_length": self.max_length}
#         resp = requests.post(self.api_url, headers=headers, json=payload, timeout=self.timeout)
#         resp.raise_for_status()
#         return resp.json()["response"]


# def _summarize_weather(weather: Optional[Dict]) -> str:
#     if not weather or "daily" not in weather:
#         return "Weather data unavailable — assume moderate conditions and pack for variability."
#     daily = weather["daily"]
#     highs = daily.get("temperature_2m_max", [])
#     lows = daily.get("temperature_2m_min", [])
#     rain = daily.get("precipitation_probability_max", [])
#     if not highs:
#         return "Weather data unavailable."
#     avg_high = sum(highs) / len(highs)
#     avg_low = sum(lows) / len(lows)
#     avg_rain = sum(rain) / len(rain) if rain else 0
#     return (
#         f"Average high {avg_high:.0f}°C, average low {avg_low:.0f}°C, "
#         f"average chance of rain {avg_rain:.0f}%."
#     )


# def build_travel_report(
#     llm: RemoteMistralLLM,
#     departure: str,
#     destination: str,
#     num_days: int,
#     visa_info: Dict,
#     weather: Optional[Dict],
# ) -> Dict[str, str]:
#     """Two-step prompt chain: day-by-day plan first, then a prep checklist
#     that reuses the plan's output as context (chaining keywords forward)."""

#     weather_summary = _summarize_weather(weather)

#     plan_prompt = (
#         f"You are a travel assistant. Create a {num_days}-day itinerary for a trip "
#         f"from {departure} to {destination}.\n"
#         f"Visa situation: {visa_info['message']}\n"
#         f"Weather during the trip: {weather_summary}\n"
#         f"Give a concise day-by-day plan (activities, pacing, any weather-related "
#         f"adjustments). Keep it practical."
#     )
#     plan = llm(plan_prompt).strip()

#     checklist_prompt = (
#         f"Based on this itinerary for a trip from {departure} to {destination}:\n"
#         f"{plan}\n\n"
#         f"Visa situation: {visa_info['message']}\n"
#         f"Weather: {weather_summary}\n\n"
#         f"List what the traveller should prepare before departure: required "
#         f"documents (visa/ETA if applicable), suggested clothing/gear given the "
#         f"weather, and other practical tips (currency, adapters, tickets, etc). "
#         f"Keep it as a short checklist."
#     )
#     checklist = llm(checklist_prompt).strip()

#     return {"plan": plan, "checklist": checklist}


# from typing import Optional, List, Dict, Any
# import requests

# try:
#     from langchain_core.language_models.llms import LLM
# except ImportError:  # older langchain versions
#     from langchain.llms.base import LLM


# class RemoteMistralLLM(LLM):
#     """LangChain-compatible wrapper around the FastAPI/ngrok endpoint on Kaggle."""

# #     api_url: str
# #     api_key: str
# #     max_length: int = 400
# #     timeout: int = 120

# #     @property
# #     def _llm_type(self) -> str:
# #         return "remote_mistral_nemo"

# #     def _call(self, prompt: str, stop: Optional[List[str]] = None, **kwargs: Any) -> str:
# #         headers = {"Authorization": f"Bearer {self.api_key}"}
# #         payload = {"prompt": prompt, "max_length": self.max_length}
# #         resp = requests.post(self.api_url, headers=headers, json=payload, timeout=self.timeout)
# #         resp.raise_for_status()
# #         return resp.json()["response"]


# # def _summarize_weather(weather: Optional[Dict]) -> str:
# #     if not weather or "daily" not in weather:
# #         return "Weather data unavailable — assume moderate conditions and pack for variability."
# #     daily = weather["daily"]
# #     highs = daily.get("temperature_2m_max", [])
# #     lows = daily.get("temperature_2m_min", [])
# #     rain = daily.get("precipitation_probability_max", [])
# #     if not highs:
# #         return "Weather data unavailable."
# #     avg_high = sum(highs) / len(highs)
# #     avg_low = sum(lows) / len(lows)
# #     avg_rain = sum(rain) / len(rain) if rain else 0

# #     prefix = (
# #         "Estimated (based on the same dates last year, since the trip is too far out "
# #         "for a live forecast)"
# #         if weather.get("_source") == "historical_estimate"
# #         else "Forecast"
# #     )
# #     return (
# #         f"{prefix}: average high {avg_high:.0f}°C, average low {avg_low:.0f}°C, "
# #         f"average chance of rain {avg_rain:.0f}%."
# #     )


# # def build_travel_report(
# #     llm: RemoteMistralLLM,
# #     departure: str,
# #     destination: str,
# #     num_days: int,
# #     visa_info: Dict,
# #     weather: Optional[Dict],
# # ) -> Dict[str, str]:
# #     """Two-step prompt chain: day-by-day plan first, then a prep checklist
# #     that reuses the plan's output as context (chaining keywords forward)."""

# #     weather_summary = _summarize_weather(weather)

# #     plan_prompt = (
# #         f"You are a travel assistant. Create a {num_days}-day itinerary for a trip "
# #         f"from {departure} to {destination}.\n"
# #         f"Visa situation: {visa_info['message']}\n"
# #         f"Weather during the trip: {weather_summary}\n"
# #         f"Give a concise day-by-day plan (activities, pacing, any weather-related "
# #         f"adjustments). Keep it practical."
# #     )
# #     plan = llm.invoke(plan_prompt).strip()

# #     checklist_prompt = (
# #         f"Based on this itinerary for a trip from {departure} to {destination}:\n"
# #         f"{plan}\n\n"
# #         f"Visa situation: {visa_info['message']}\n"
# #         f"Weather: {weather_summary}\n\n"
# #         f"List what the traveller should prepare before departure: required "
# #         f"documents (visa/ETA if applicable), suggested clothing/gear given the "
# #         f"weather, and other practical tips (currency, adapters, tickets, etc). "
# #         f"Keep it as a short checklist."
# #     )
# #     checklist = llm.invoke(checklist_prompt).strip()

# #     return {"plan": plan, "checklist": checklist}
# # from typing import Optional, List, Dict, Any
# # import requests

# # try:
# #     from langchain_core.language_models.llms import LLM
# # except ImportError:  # older langchain versions
# #     from langchain.llms.base import LLM


# # class RemoteMistralLLM(LLM):
# #     """LangChain-compatible wrapper around the FastAPI/ngrok endpoint on Kaggle."""

# #     api_url: str
# #     api_key: str
# #     max_length: int = 400
# #     timeout: int = 120

# #     @property
# #     def _llm_type(self) -> str:
# #         return "remote_mistral_nemo"

# #     def _call(self, prompt: str, stop: Optional[List[str]] = None, **kwargs: Any) -> str:
# #         headers = {"Authorization": f"Bearer {self.api_key}"}
# #         payload = {"prompt": prompt, "max_length": self.max_length}
# #         resp = requests.post(self.api_url, headers=headers, json=payload, timeout=self.timeout)
# #         resp.raise_for_status()
# #         return resp.json()["response"]


# # def _summarize_weather(weather: Optional[Dict]) -> str:
# #     if not weather or weather.get("avg_high") is None:
# #         return "Weather data unavailable — assume moderate conditions and pack for variability."

# #     avg_high = weather["avg_high"]
# #     avg_low = weather["avg_low"]

# #     if weather.get("source") == "historical_estimate":
# #         prefix = "Estimated (based on the same dates last year, since the trip is too far out for a live forecast)"
# #         rain_part = (
# #             f"average rainfall {weather['avg_rain_mm']:.1f}mm/day"
# #             if weather.get("avg_rain_mm") is not None
# #             else "rainfall data unavailable"
# #         )
# #     else:
# #         prefix = "Forecast"
# #         rain_part = (
# #             f"average chance of rain {weather['avg_rain_probability_pct']:.0f}%"
# #             if weather.get("avg_rain_probability_pct") is not None
# #             else "rain chance unavailable"
# #         )

# #     return f"{prefix}: average high {avg_high:.0f}°C, average low {avg_low:.0f}°C, {rain_part}."


# # def build_travel_report(
# #     llm: RemoteMistralLLM,
# #     departure: str,
# #     destination: str,
# #     num_days: int,
# #     visa_info: Dict,
# #     weather: Optional[Dict],
# # ) -> Dict[str, str]:
# #     """Two-step prompt chain: day-by-day plan first, then a prep checklist
# #     that reuses the plan's output as context (chaining keywords forward)."""

# #     weather_summary = _summarize_weather(weather)

# #     plan_prompt = (
# #         f"You are a travel assistant. Create a {num_days}-day itinerary for a trip "
# #         f"from {departure} to {destination}.\n"
# #         f"Visa situation: {visa_info['message']}\n"
# #         f"Weather during the trip: {weather_summary}\n"
# #         f"Give a concise day-by-day plan (activities, pacing, any weather-related "
# #         f"adjustments). Keep it practical."
# #     )
# #     plan = llm.invoke(plan_prompt).strip()

# #     checklist_prompt = (
# #         f"Based on this itinerary for a trip from {departure} to {destination}:\n"
# #         f"{plan}\n\n"
# #         f"Visa situation: {visa_info['message']}\n"
# #         f"Weather: {weather_summary}\n\n"
# #         f"List what the traveller should prepare before departure: required "
# #         f"documents (visa/ETA if applicable), suggested clothing/gear given the "
# #         f"weather, and other practical tips (currency, adapters, tickets, etc). "
# #         f"Keep it as a short checklist."
# #     )
# #     checklist = llm.invoke(checklist_prompt).strip()

# #     return {"plan": plan, "checklist": checklist}
# from typing import Optional, List, Dict, Any
# import requests

# try:
#     from langchain_core.language_models.llms import LLM
# except ImportError:  # older langchain versions
#     from langchain.llms.base import LLM


# class RemoteMistralLLM(LLM):
#     """LangChain-compatible wrapper around the FastAPI/ngrok endpoint on Kaggle."""

#     api_url: str
#     api_key: str
#     max_length: int = 400
#     timeout: int = 120

#     @property
#     def _llm_type(self) -> str:
#         return "remote_mistral_nemo"

#     def _call(self, prompt: str, stop: Optional[List[str]] = None, **kwargs: Any) -> str:
#         headers = {"Authorization": f"Bearer {self.api_key}"}
#         payload = {"prompt": prompt, "max_length": self.max_length}
#         resp = requests.post(self.api_url, headers=headers, json=payload, timeout=self.timeout)
#         resp.raise_for_status()
#         return resp.json()["response"]


# def _summarize_weather(weather: Optional[Dict]) -> str:
#     if not weather or weather.get("avg_high") is None:
#         return "Weather data unavailable — assume moderate conditions and pack for variability."

#     avg_high = weather["avg_high"]
#     avg_low = weather["avg_low"]

#     if weather.get("source") == "historical_estimate":
#         prefix = "Estimated (based on the same dates last year, since the trip is too far out for a live forecast)"
#         rain_part = (
#             f"average rainfall {weather['avg_rain_mm']:.1f}mm/day"
#             if weather.get("avg_rain_mm") is not None
#             else "rainfall data unavailable"
#         )
#     else:
#         prefix = "Forecast"
#         rain_part = (
#             f"average chance of rain {weather['avg_rain_probability_pct']:.0f}%"
#             if weather.get("avg_rain_probability_pct") is not None
#             else "rain chance unavailable"
#         )

#     return f"{prefix}: average high {avg_high:.0f}°C, average low {avg_low:.0f}°C, {rain_part}."


# def build_travel_report(
#     llm: RemoteMistralLLM,
#     departure: str,
#     destination: str,
#     num_days: int,
#     visa_info: Dict,
#     weather: Optional[Dict],
# ) -> Dict[str, str]:
#     """Two-step prompt chain: day-by-day plan first, then a prep checklist
#     that reuses the plan's output as context (chaining keywords forward)."""

#     weather_summary = _summarize_weather(weather)

#     plan_prompt = (
#         f"Write a {num_days}-day travel itinerary for a trip FROM {departure} TO {destination}. "
#         f"The entire trip must take place in {destination}. Do not mention any other "
#         f"country as a destination, and do not invent a multi-country route.\n\n"
#         f"Visa situation: {visa_info['message']}\n"
#         f"Weather during the trip: {weather_summary}\n\n"
#         f"Give a concise day-by-day plan for {destination} only (activities, pacing, "
#         f"any weather-related adjustments). Keep it practical."
#     )
#     plan = llm.invoke(plan_prompt).strip()

#     checklist_prompt = (
#         f"Based on this itinerary for a trip FROM {departure} TO {destination}:\n"
# #         f"{plan}\n\n"
# #         f"Visa situation: {visa_info['message']}\n"
# #         f"Weather: {weather_summary}\n\n"
# #         f"List what a traveller from {departure} should prepare before departure: "
# #         f"required documents (visa/ETA if applicable), suggested clothing/gear given "
# #         f"the weather, and other practical tips (currency, adapters, tickets, etc). "
# #         f"Keep it as a short checklist."
# #     )
# #     checklist = llm.invoke(checklist_prompt).strip()

# #     return {"plan": plan, "checklist": checklist}

# from typing import Optional, List, Dict, Any
# import requests

# try:
#     from langchain_core.language_models.llms import LLM
# except ImportError:  # older langchain versions
#     from langchain.llms.base import LLM


# class RemoteMistralLLM(LLM):
#     """LangChain-compatible wrapper around the FastAPI/ngrok endpoint on Kaggle."""

#     api_url: str
#     api_key: str
#     max_length: int = 400
#     timeout: int = 120

#     @property
#     def _llm_type(self) -> str:
#         return "remote_mistral_nemo"

#     def _call(self, prompt: str, stop: Optional[List[str]] = None, **kwargs: Any) -> str:
#         headers = {"Authorization": f"Bearer {self.api_key}"}
#         payload = {"prompt": prompt, "max_length": self.max_length}
#         resp = requests.post(self.api_url, headers=headers, json=payload, timeout=self.timeout)
#         resp.raise_for_status()
#         return resp.json()["response"]


# def _summarize_weather(weather: Optional[Dict]) -> str:
#     if not weather or weather.get("avg_high") is None:
#         return "Weather data unavailable — assume moderate conditions and pack for variability."

#     avg_high = weather["avg_high"]
#     avg_low = weather["avg_low"]

#     if weather.get("source") == "historical_estimate":
#         prefix = "Estimated (based on the same dates last year, since the trip is too far out for a live forecast)"
#         rain_part = (
#             f"average rainfall {weather['avg_rain_mm']:.1f}mm/day"
#             if weather.get("avg_rain_mm") is not None
#             else "rainfall data unavailable"
#         )
#     else:
#         prefix = "Forecast"
#         rain_part = (
#             f"average chance of rain {weather['avg_rain_probability_pct']:.0f}%"
#             if weather.get("avg_rain_probability_pct") is not None
#             else "rain chance unavailable"
#         )

#     return f"{prefix}: average high {avg_high:.0f}°C, average low {avg_low:.0f}°C, {rain_part}."


# def build_travel_report(
#     llm: RemoteMistralLLM,
#     departure: str,
#     destination: str,
#     num_days: int,
#     visa_info: Dict,
#     weather: Optional[Dict],
# ) -> Dict[str, str]:
#     """Two-step prompt chain: day-by-day plan first, then a prep checklist
#     that reuses the plan's output as context (chaining keywords forward)."""

#     weather_summary = _summarize_weather(weather)

#     plan_prompt = (
#         f"Write a {num_days}-day travel itinerary for a trip FROM {departure} TO {destination}. "
#         f"The entire trip must take place in {destination}. Do not mention any other "
#         f"country as a destination, and do not invent a multi-country route.\n\n"
#         f"Visa situation: {visa_info['message']}\n"
#         f"Weather during the trip: {weather_summary}\n\n"
#         f"Give a concise day-by-day plan for {destination} only (activities, pacing, "
#         f"any weather-related adjustments). Keep it practical."
#     )
#     plan = llm.invoke(plan_prompt).strip()

#     # Truncate when embedding the plan into the next prompt — keeps input
#     # token count lower, which matters more now that we're not quantizing.
#     plan_for_context = plan if len(plan) <= 1500 else plan[:1500] + "..."

#     checklist_prompt = (
#         f"Based on this itinerary for a trip FROM {departure} TO {destination}:\n"
#         f"{plan_for_context}\n\n"
#         f"Visa situation: {visa_info['message']}\n"
#         f"Weather: {weather_summary}\n\n"
#         f"List what a traveller from {departure} should prepare before departure: "
#         f"required documents (visa/ETA if applicable), suggested clothing/gear given "
#         f"the weather, and other practical tips (currency, adapters, tickets, etc). "
#         f"Keep it as a short checklist."
#     )
#     checklist = llm.invoke(checklist_prompt).strip()

#     return {"plan": plan, "checklist": checklist}

# from typing import Optional, List, Dict, Any
# import requests

# try:
#     from langchain_core.language_models.llms import LLM
# except ImportError:  # older langchain versions
#     from langchain.llms.base import LLM


# class RemoteMistralLLM(LLM):
#     """LangChain-compatible wrapper around the FastAPI/ngrok endpoint on Kaggle."""

#     api_url: str
#     api_key: str
#     max_length: int = 400
#     timeout: int = 120

#     @property
#     def _llm_type(self) -> str:
#         return "remote_mistral_nemo"

#     def _call(self, prompt: str, stop: Optional[List[str]] = None, **kwargs: Any) -> str:
#         headers = {"Authorization": f"Bearer {self.api_key}"}
#         payload = {"prompt": prompt, "max_length": self.max_length}
#         resp = requests.post(self.api_url, headers=headers, json=payload, timeout=self.timeout)
#         resp.raise_for_status()
#         return resp.json()["response"]


# def summarize_weather(weather: Optional[Dict]) -> str:
#     if not weather or weather.get("avg_high") is None:
#         return "Weather data unavailable — assume moderate conditions and pack for variability."

#     avg_high = weather["avg_high"]
#     avg_low = weather["avg_low"]

#     if weather.get("source") == "historical_estimate":
#         prefix = "Estimated (based on the same dates last year, since the trip is too far out for a live forecast)"
#         rain_part = (
#             f"average rainfall {weather['avg_rain_mm']:.1f}mm/day"
#             if weather.get("avg_rain_mm") is not None
#             else "rainfall data unavailable"
#         )
#     else:
#         prefix = "Forecast"
#         rain_part = (
#             f"average chance of rain {weather['avg_rain_probability_pct']:.0f}%"
#             if weather.get("avg_rain_probability_pct") is not None
#             else "rain chance unavailable"
#         )

#     return f"{prefix}: average high {avg_high:.0f}°C, average low {avg_low:.0f}°C, {rain_part}."


# def build_travel_report(
#     llm: RemoteMistralLLM,
#     departure: str,
#     destination: str,
#     num_days: int,
#     visa_info: Dict,
#     weather: Optional[Dict],
# ) -> Dict[str, str]:
#     """Two-step prompt chain: day-by-day plan first, then a prep checklist
#     that reuses the plan's output as context (chaining keywords forward)."""

#     weather_summary = summarize_weather(weather)

#     plan_prompt = (
#         f"Write a {num_days}-day travel itinerary for a trip FROM {departure} TO {destination}. "
#         f"The entire trip must take place in {destination}. Do not mention any other "
#         f"country as a destination, and do not invent a multi-country route.\n\n"
#         f"Visa situation: {visa_info['message']}\n"
#         f"Weather during the trip: {weather_summary}\n\n"
#         f"Give a concise day-by-day plan for {destination} only (activities, pacing, "
#         f"any weather-related adjustments). Keep it practical."
#     )
#     plan = llm.invoke(plan_prompt).strip()

#     # Truncate when embedding the plan into the next prompt — keeps input
#     # token count lower, which matters more now that we're not quantizing.
#     plan_for_context = plan if len(plan) <= 1500 else plan[:1500] + "..."

#     checklist_prompt = (
#         f"Based on this itinerary for a trip FROM {departure} TO {destination}:\n"
#         f"{plan_for_context}\n\n"
#         f"Visa situation: {visa_info['message']}\n"
#         f"Weather: {weather_summary}\n\n"
#         f"List what a traveller from {departure} should prepare before departure: "
#         f"required documents (visa/ETA if applicable), suggested clothing/gear given "
#         f"the weather, and other practical tips (currency, adapters, tickets, etc). "
#         f"Keep it as a short checklist."
#     )
#     checklist = llm.invoke(checklist_prompt).strip()

#     return {"plan": plan, "checklist": checklist}


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
    max_length: int = 2000  # //change for remove random
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


def summarize_weather(weather: Optional[Dict]) -> str:
    if not weather or weather.get("avg_high") is None:
        return "Weather data unavailable — assume moderate conditions and pack for variability."

    avg_high = weather["avg_high"]
    avg_low = weather["avg_low"]

    if weather.get("source") == "historical_estimate":
        prefix = "Estimated (based on the same dates last year, since the trip is too far out for a live forecast)"
        rain_part = (
            f"average rainfall {weather['avg_rain_mm']:.1f}mm/day"
            if weather.get("avg_rain_mm") is not None
            else "rainfall data unavailable"
        )
    else:
        prefix = "Forecast"
        rain_part = (
            f"average chance of rain {weather['avg_rain_probability_pct']:.0f}%"
            if weather.get("avg_rain_probability_pct") is not None
            else "rain chance unavailable"
        )

    return f"{prefix}: average high {avg_high:.0f}°C, average low {avg_low:.0f}°C, {rain_part}."


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

    weather_summary = summarize_weather(weather)

    plan_prompt = (
        f"Write a {num_days}-day travel itinerary for a trip FROM {departure} TO {destination}. "
        f"The entire trip must take place in {destination}. Do not mention any other "
        f"country as a destination, and do not invent a multi-country route.\n\n"
        f"Visa situation: {visa_info['message']}\n"
        f"Weather during the trip: {weather_summary}\n\n"
        f"Give a concise day-by-day plan for {destination} only (activities, pacing, "
        f"any weather-related adjustments). Keep it practical."
    )
    plan = llm.invoke(plan_prompt).strip()

    # Truncate when embedding the plan into the next prompt — keeps input
    # token count lower, which matters more now that we're not quantizing.
    if len(plan) <= 1500:  # //change for remove random
        plan_for_context = plan  # //change for remove random
    else:  # //change for remove random
        last_sentence_end = plan.rfind('.', 0, 1500)  # //change for remove random
        if last_sentence_end != -1:  # //change for remove random
            plan_for_context = plan[:last_sentence_end + 1] + "..."  # //change for remove random
        else:  # //change for remove random
            plan_for_context = plan[:1500] + "..."  # //change for remove random

    checklist_prompt = (
        f"Based on this itinerary for a trip FROM {departure} TO {destination}:\n"
        f"{plan_for_context}\n\n"
        f"Visa situation: {visa_info['message']}\n"
        f"Weather: {weather_summary}\n\n"
        f"List what a traveller from {departure} should prepare before departure: "
        f"required documents (visa/ETA if applicable), suggested clothing/gear given "
        f"the weather, and other practical tips (currency, adapters, tickets, etc). "
        f"Keep it as a short checklist."
    )
    checklist = llm.invoke(checklist_prompt).strip()

    return {"plan": plan, "checklist": checklist}
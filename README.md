# AI Travel Assistant

An intelligent travel planning application designed to eliminate trip-planning friction by automating itineraries, verifying visa requirements, and providing weather-informed packing guides.

## Key Features

* **Personalized Itinerary Generation:** Uses a two-step prompt chain to build custom day-by-day travel plans and practical prep checklists.
* **Deterministic Visa Lookup:** Leverages Pandas to instantly cross-reference passport rules and entry conditions from a structured dataset.
* **Smart Weather Integration:** Connects to the Open-Meteo API to fetch live forecasts for upcoming trips or historical climate data for trips further out.
* **Remote Model Inference:** Implements a custom LangChain wrapper (`RemoteMistralLLM`) to connect application logic to a remote model endpoint.

## Tech Stack

* **Framework:** LangChain, Streamlit
* **AI Model:** Mistral AI
* **Backend & Networking:** FastAPI, ngrok, Pandas
* **APIs:** Open-Meteo (Geocoding, Forecast, and Archive)


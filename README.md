<img width="1280" height="677" alt="photo_2026-07-28_22-55-40" src="https://github.com/user-attachments/assets/2ad7de77-6724-4b2c-8022-0e3af52d2470" />
<img width="1280" height="670" alt="photo_2026-07-28_22-53-44" src="https://github.com/user-attachments/assets/3c1a0c0b-6eed-4178-8ad2-0d3eaa68f7a4" />
<img width="1280" height="639" alt="photo_2026-07-28_22-53-01" src="https://github.com/user-attachments/assets/0775c00d-f416-43d7-9949-7f880d322726" />


https://github.com/user-attachments/assets/d3e45975-52fe-410c-94f8-6b77e1f11f95




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


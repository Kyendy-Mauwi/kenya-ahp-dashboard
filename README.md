# 🇰🇪 Kenya Affordable Housing Programme (AHP) Monitor

A comprehensive full-stack data dashboard designed to track the progress of the **Boma Yangu** initiative across all 47 counties. This tool provides transparency for Government Overseers, project insights for Private Developers, and an affordability engine for Kenyan Citizens.

https://kenya-ahp-dashboard.streamlit.app/

---

## 🚀 Key Features

### 1. National Project Directory
- **Exhaustive Mapping:** Tracks 100+ active and planned projects including flagship sites like *Starehe Point*, *Pangani*, and *Kimumu AMS*.
- **Intelligent Search:** Filter by County or Project Name to see localized unit counts and construction status.

### 2. Tenant Purchase Scheme (TPS) Calculator
- **Affordability Logic:** Uses the official **7% fixed interest rate** over a **25-year period**.
- **Eligibility Sorting:** Automatically categorizes users into *Social*, *Low-Cost*, or *Affordable* housing brackets based on monthly income.

### 3. Economic Impact Tracker (BETA)
- **MSME Integration:** Monitors the **KES 11B+** ring-fenced for Jua Kali artisans.
- **Supply Chain Visibility:** Tracks the local production of the 79 reserved building items (doors, windows, etc.).

---

## 🛠️ Tech Stack

* **Language:** Python 3.12
* **Framework:** [Streamlit](https://streamlit.io/) (Dashboard UI)
* **Visuals:** [Plotly](https://plotly.com/) & [Pandas](https://pandas.pydata.org/) (Data Processing)
* **Styling:** Custom `.streamlit/config.toml` using the Kenyan National Palette (Green & Gold).

---

## 📂 Project Structure

```text
kenya-ahp-monitor/
├── .streamlit/          # Theme configuration (Green/Gold/Dark Mode)
├── data/                # Geographic and mock data storage
├── src/                 # Logic modules
│   ├── calculator.py    # TPS amortization & eligibility engine
│   ├── scraper.py       # National project directory & MSME data
│   └── ui_components.py # Plotly & Gauge chart templates
├── app.py               # Main Entry Point
└── requirements.txt     # Dependency list

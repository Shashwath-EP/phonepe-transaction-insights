# 📊 PhonePe Transaction Insights Dashboard

An end-to-end data analytics project that extracts, processes, and visualizes PhonePe transaction data to uncover meaningful business insights.

---

## 🚀 Project Overview

This project analyzes digital payment data from PhonePe Pulse to understand transaction trends, user behavior, and geographical distribution across India.

It includes:
- Data Extraction from JSON  
- Data Transformation using Python  
- Storage using SQLite  
- Interactive Dashboard using Streamlit  

---

## 🎯 Objectives

- Analyze transaction patterns across states and districts  
- Identify top-performing regions  
- Understand payment category trends  
- Build an interactive visualization dashboard  

---

## 📂 Project Structure

```bash
phonepe_project/
│
├── dashboard/
│   ├── app.py
│   └── india_states.json
│
├── scripts/
│   ├── transform.py
│   └── load.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── phonepe.db
├── requirements.txt
└── README.md
```

## 🛠️ Tech Stack

- **Python**
- **Pandas**
- **SQLite**
- **Streamlit**
- **Plotly**

## ⚙️ Data Pipeline (ETL)

### 1. Extract
- Data is sourced from PhonePe Pulse GitHub repository
- JSON files containing transaction data are parsed

### 2. Transform
- Data cleaned and structured using Pandas
- Missing values handled
- Aggregations performed

### 3. Load
- Data stored in SQLite database (`phonepe.db`)
- Tables:
  - aggregated_transaction
  - aggregated_user
  - top_transaction

## 🖥️ How to Run Locally

```bash
# Clone repository
git clone https://github.com/Shashwath-EP/phonepe-transaction-insights.git

# Navigate to project folder
cd phonepe_project

# Load data into SQLite
python scripts/load.py

# Run dashboard
streamlit run dashboard/app.py

Add predictive modeling
```

## 📊 Dashboard Features

- 📌 KPI Metrics (Transactions & Amount)
- 📈 Top States Analysis
- 🧭 District-Level Insights
- 📊 Transaction Type Distribution
- 🌍 India Choropleth Map
- 📅 Year-wise Filtering

## 📈 Key Insights

- Maharashtra and Karnataka dominate transaction volume  
- Digital payments show steady growth  
- Urban districts have higher activity  
- Few states contribute majority of transactions  


## 🌐 Deployment

The project is deployed using Streamlit Community Cloud.

https://phonepe-transaction-insights-wnyxutj3rxp9wxr9vvqee2.streamlit.app/

## 📦 Requirements

- streamlit
- pandas
- plotly
- numpy

## 🧠 Learnings

Built end-to-end ETL pipeline

Worked with real-world JSON data

Designed interactive dashboards

Solved data cleaning and mapping challenges

Implemented offline geo-visualization

## 📌 Future Improvements

Add real-time data updates

Enhance UI/UX

Integrate advanced analytics

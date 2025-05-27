
# 📘 Real-Time Stock Data Pipeline with Kafka, PySpark, Snowflake, and Power BI

## 🔧 Overview

This project demonstrates a **real-time cloud-native data pipeline** that streams live stock market data using **Kafka**, processes it using **PySpark**, stores it in **Snowflake**, and visualizes insights in **Power BI**. It simulates a production-grade workflow integrating modern tools in the data engineering ecosystem.

---

## 🧱 Tech Stack

- **Data Ingestion:** yfinance, Kafka, Confluent Cloud  
- **Stream Processing:** PySpark Structured Streaming (Databricks / local)  
- **Storage:** Snowflake  
- **Visualization:** Power BI  
- **Cloud Services Explored:** Databricks, AWS Glue, AWS S3, EC2, Confluent Cloud  
- **Alternatives Tested:** Local Kafka, Confluent Kafka CLI, Snowflake Python connector  

---

## 📈 Features

- Real-time stock data fetch using Yahoo Finance API (`yfinance`)
- Kafka producer streams data into topic `realtime_stock_data`
- Kafka consumer reads and writes data to Snowflake
- Automated CSV generation for Power BI
- Daily historical data for the past 1 year from Yahoo Finance
- Power BI dashboard with clean KPI visuals

---

## 📊 Key KPIs in Dashboard

- Daily Close Price Trend  
- 7-Day Moving Average  
- Daily % Change  
- Total Volume Traded  
- High-Low Spread  
- Min/Max Prices Over Period  

---

## 📁 Project Structure

```
.
├── stock_producer.py                 # Streams stock data to Kafka
├── kafka_to_snowflake_consumer.py   # Reads Kafka & inserts into Snowflake
├── daily_stock_data_1year.csv       # Exported CSV for Power BI
├── README.md                        # Project documentation (this file)
└── dashboard.pbix                   # Power BI Dashboard (optional)
```

---

## 🚀 How to Run

```bash
# Kafka Producer
python stock_producer.py

# Kafka Consumer → Snowflake
python kafka_to_snowflake_consumer.py
```

Open Power BI → Import `daily_stock_data_1year.csv`  
Or connect directly via FMP API for live data.

---

## 🧠 Learning Outcomes

- Built an end-to-end streaming data pipeline
- Hands-on with Kafka (local & cloud), PySpark, Snowflake, and Power BI
- Solved real-world integration challenges (SSL, PEM, Hadoop, VPC access)
- Learned how to move pipelines from local to cloud

---

## ✅ Future Work

- Dockerize producer and consumer
- Auto-schedule jobs with Airflow or AWS Lambda
- Add predictive analytics (ARIMA, Prophet)
- Integrate social sentiment analysis (Reddit/Twitter)

---

## 🤝 Credits

Stock data via [yfinance](https://yfinance.yahoo.com) and [FMP API](https://financialmodelingprep.com)  
Built and tested by **You**

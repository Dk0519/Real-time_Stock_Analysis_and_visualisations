
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Real-Time Stock Data Pipeline</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
            line-height: 1.6;
            text-align: center;
        }
        h1, h2, h3 { color: #2c3e50; }
        code {
            background-color: #f4f4f4;
            padding: 2px 4px;
            border-radius: 4px;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            text-align: left;
            display: inline-block;
        }
        ul {
            display: inline-block;
            text-align: left;
            margin: 0 auto;
        }
        p {
            max-width: 800px;
            margin: auto;
        }
    </style>
</head>
<body>

<h1>📘 Real-Time Stock Data Pipeline with Kafka, PySpark, Snowflake, and Power BI</h1>

<h2>🔧 Overview</h2>
<p>
This project demonstrates a <strong>real-time cloud-native data pipeline</strong> that streams live stock market data using <strong>Kafka</strong>, processes it using <strong>PySpark</strong>,
stores it in <strong>Snowflake</strong>, and visualizes insights in <strong>Power BI</strong>. It simulates a production-grade workflow integrating modern tools in the data engineering ecosystem.
</p>

<h2>🧱 Tech Stack</h2>
<ul>
    <li><strong>Data Ingestion:</strong> yfinance, Kafka, Confluent Cloud</li>
    <li><strong>Stream Processing:</strong> PySpark Structured Streaming (Databricks / local)</li>
    <li><strong>Storage:</strong> Snowflake</li>
    <li><strong>Visualization:</strong> Power BI</li>
    <li><strong>Cloud Services Explored:</strong> Databricks, AWS Glue, AWS S3, EC2, Confluent Cloud</li>
    <li><strong>Alternatives Tested:</strong> Local Kafka, Confluent Kafka CLI, Snowflake Python connector</li>
</ul>

<h2>📈 Features</h2>
<ul>
    <li>Real-time stock data fetch using Yahoo Finance API (yfinance)</li>
    <li>Kafka producer streams data into topic <code>realtime_stock_data</code></li>
    <li>Kafka consumer reads and writes data to Snowflake</li>
    <li>Automated CSV generation for Power BI</li>
    <li>Daily historical data for the past 1 year from Yahoo Finance</li>
    <li>Power BI dashboard with clean KPI visuals</li>
</ul>

<h2>📊 Key KPIs in Dashboard</h2>
<ul>
    <li>Daily Close Price Trend</li>
    <li>7-Day Moving Average</li>
    <li>Daily % Change</li>
    <li>Total Volume Traded</li>
    <li>High-Low Spread</li>
    <li>Min/Max Prices Over Period</li>
</ul>

<h2>📁 Project Structure</h2>
<pre>
.
├── stock_producer.py                 # Streams stock data to Kafka
├── kafka_to_snowflake_consumer.py   # Reads Kafka & inserts into Snowflake
├── daily_stock_data_1year.csv       # Exported CSV for Power BI
├── README.html                      # Project documentation (this file)
└── dashboard.pbix                   # Power BI Dashboard (optional)
</pre>

<h2>🚀 How to Run</h2>
<pre>
# Kafka Producer
python stock_producer.py

# Kafka Consumer → Snowflake
python kafka_to_snowflake_consumer.py
</pre>
<p>Open Power BI, load <code>daily_stock_data_1year.csv</code>, and create visuals or use the FMP API connection.</p>

<h2>🧠 Learning Outcomes</h2>
<ul>
    <li>Built an end-to-end streaming data pipeline</li>
    <li>Hands-on with Kafka (local & cloud), PySpark, Snowflake, and Power BI</li>
    <li>Solved real-world integration challenges (SSL, PEM, Hadoop, VPC access)</li>
    <li>Learned how to move pipelines from local to cloud</li>
</ul>

<h2>✅ Future Work</h2>
<ul>
    <li>Dockerize producer and consumer</li>
    <li>Auto-schedule jobs with Airflow or AWS Lambda</li>
    <li>Add predictive analytics (ARIMA, Prophet)</li>
    <li>Integrate social sentiment analysis (Reddit/Twitter)</li>
</ul>

<h2>🤝 Credits</h2>
<p>Stock data via <a href="https://yfinance.yahoo.com">yfinance</a> and <a href="https://financialmodelingprep.com">FMP API</a>.<br>Built and tested by <strong>You</strong>.</p>

</body>
</html>

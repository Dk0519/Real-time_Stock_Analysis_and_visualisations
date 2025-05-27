from kafka import KafkaProducer
import yfinance as yf
import json
import time

KAFKA_TOPIC = "realtime_stock_data"
KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"
TICKERS = ["AAPL", "TSLA", "INFY", "RELIANCE.NS"]

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

print(f"🚀 Starting producer for tickers: {TICKERS}")
while True:
    for ticker in TICKERS:
        try:
            data = yf.Ticker(ticker).history(period="1d", interval="1m").tail(1)
            if not data.empty:
                record = {
                    "ticker": ticker,
                    "datetime": data.index[0].strftime("%Y-%m-%d %H:%M:%S"),
                    "open": round(data["Open"].iloc[0], 2),
                    "high": round(data["High"].iloc[0], 2),
                    "low": round(data["Low"].iloc[0], 2),
                    "close": round(data["Close"].iloc[0], 2),
                    "volume": int(data["Volume"].iloc[0])
                }
                producer.send(KAFKA_TOPIC, record)
                print(f"✅ Sent: {record}")
        except Exception as e:
            print(f"❌ Error for {ticker}: {e}")
    time.sleep(60)

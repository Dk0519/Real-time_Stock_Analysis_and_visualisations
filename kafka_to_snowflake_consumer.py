from kafka import KafkaConsumer
import snowflake.connector
import json

# Snowflake connection
conn = snowflake.connector.connect(
    user='DIVYANSHU0519',
    password='Divyanshu@0519',
    account='QH13814.ap-southeast-1',
    warehouse='COMPUTE_WH',
    database='STOCK_DB',
    schema='PUBLIC'
)

cursor = conn.cursor()

# Kafka Consumer
consumer = KafkaConsumer(
    'realtime_stock_data',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("🟢 Kafka Consumer started...")

# Consume messages
for message in consumer:
    data = message.value
    print(f"📥 Consumed: {data}")
    
    # Insert into Snowflake
    cursor.execute("""
        INSERT INTO stock_table (ticker, datetime, open, high, low, close, volume)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        data['ticker'],
        data['datetime'],
        data['open'],
        data['high'],
        data['low'],
        data['close'],
        data['volume']
    ))

    print("✅ Inserted into Snowflake")

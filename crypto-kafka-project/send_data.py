from kafka import KafkaProducer
import json
import time
import random

# Kafka ile bağlantı kur
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Rastgele sahte veri üret
def generate_fake_price():
    price = round(random.uniform(60000, 70000), 2)
    return {
        "bitcoin": {
            "usd": price
        }
    }

# Sürekli veri gönder
while True:
    data = generate_fake_price()
    print(f"Sending data: {data}")
    producer.send('crypto-topic', value=data)
    time.sleep(5)

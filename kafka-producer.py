from kafka import KafkaProducer
import json
import time

# Kafka broker
bootstrap_servers = ['localhost:9092']

# Create Kafka producer
producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                         api_version=(0, 10, 1)
                         )

# Produce sample data
import random
Names = ["Khayyon", "Parker", "Keith", "Tyler", "Nyla", "Brian", "Georgia", "Bry", "Nu"]
for i in range(100):
    data = {"Name": random.choice(Names), "Age": i, "Gender": "Male" if i % 2 == 0 else "Female"}
    producer.send('quickstart-events', value=data)
    # time.sleep(1)

# Close producer
producer.close()
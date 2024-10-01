from kafka import KafkaConsumer

def consume_invoices():
    # consumer = KafkaConsumer('sample-data', bootstrap_servers='localhost:9092', auto_offset_reset='earliest')
    consumer = KafkaConsumer('quickstart-events', bootstrap_servers='localhost:9092', auto_offset_reset='earliest')
    for message in consumer:
        msg_content = message.value.decode('utf-8')
        print(msg_content) 
    consumer.close()

consume_invoices()
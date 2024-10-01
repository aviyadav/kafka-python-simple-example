from kafka import KafkaProducer
import pandas as pd

def produce_invoices():
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    csv_file = 'SampleCSVFile.csv'
    
    # Read the CSV file as a string
    with open(csv_file, 'r') as file:
        csv_content = file.read()

    # Send the CSV content as a message value
    producer.send('sample-data', value=csv_content.encode("UTF-8"))
    
    producer.flush()
    producer.close()

produce_invoices()
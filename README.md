# kafka-python-simple-example

## Kafka commands

Generate a Cluster UUID
```
KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"
```

Format Log Directories
```
bin/kafka-storage.sh format --standalone -t $KAFKA_CLUSTER_ID -c config/server.properties
```

#### start kafka server
```
bin/kafka-server-start.sh config/server.properties
```

#### list topics
```
bin/kafka-topics.sh --list --bootstrap-server localhost:9092
```

#### create topic
```
bin/kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092
```

#### describe topic
```
bin/kafka-topics.sh --describe --topic quickstart-events --bootstrap-server localhost:9092
```

#### Write some event to topic
```
bin/kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092
```

#### Consume events from topic from begining <offset>
```
bin/kafka-console-consumer.sh --topic quickstart-events --from-beginning --bootstrap-server localhost:9092

bin/kafka-console-consumer.sh --topic <any topic name> --from-beginning --bootstrap-server localhost:9092
```

#### delete topic
```
bin/kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic  quickstart-events
```

------stop
#### start kafka server
```
bin/kafka-server-stop.sh config/server.properties
```

## Run example

1. create venv
   ```
    python -m venv .venv
   ```
3. install dependencies
   ```
   pip install -r requirements.txt
   ```
4. run
   ```
   python producer.py
   python consumer.py
   ```

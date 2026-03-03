import json
import uuid


from confluent_kafka import Producer

producer_config = {
    "bootstrap.servers": "localhost:9092"
}

producer = Producer  (producer_config)

## This is what an event looks like . Its a Json object
order = {
    "order_id": str(uuid.uuid4()),
    "user": "lara",
    "item": "frozen yogurt",
    "quantity": 10
}

json.dumps(order).encode("utf-8")
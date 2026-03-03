import json
import uuid


from confluent_kafka import Producer

producer_config = {
    "bootstrap.servers": "localhost:9092"
}

producer = Producer  (producer_config)

def delivery_report(err,msg):
    if err:
        print(f"Delivery failed: {err}")

    else:
        print(f"Delivered {msg.vaule().decode("utf-8")}")    
    

## This is what an event looks like . Its a Json object
order = {
    "order_id": str(uuid.uuid4()),
    "user": "lara",
    "item": "frozen yogurt",
    "quantity": 10
}
## This code turns the Json into a strng  and then to Bytes so Kafak can read it 
vaule = json.dumps(order).encode("utf-8")

producer.produce(
        topic="orders",
        vaule=value,
        callback=delivery_report)

#Good for clean code. Send Kafka order in batches if there alot. If it crashes the Flush forces them to send 
producer.flush()
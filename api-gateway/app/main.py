from fastapi import FastAPI
from confluent_kafka import Producer, Consumer, KafkaException, KafkaError
from random import choice
import sys
import threading

app = FastAPI()

producer_config = {
        # User-specific properties that you must set
        'bootstrap.servers': 'kafka:9093',
        'acks':              'all'
}

consumer_config = {
    'bootstrap.servers': 'kafka:9093',
    'group.id': 'foo',
    'auto.offset.reset': 'earliest'
}

# Create Producer instance
producer = Producer(producer_config)
consumer = Consumer(consumer_config)

def delivery_callback(err, msg):
    if err:
        print('ERROR: Message failed delivery: {}'.format(err))
    else:
        print("Produced event to topic {topic}: key = {key:12} value = {value:12}".format(
            topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))

# Produce data by selecting random values from these lists.
topic = "test"
user_ids = ['eabara', 'jsmith', 'sgarcia', 'jbernard', 'htanaka', 'awalther']
products = ['book', 'alarm clock', 't-shirts', 'gift card', 'batteries']


@app.get("/")
async def root():
    return {"message": "it def works now1234"}

@app.get("/consent-granted")
async def conset_granted():
    print("hi")
    # Send a consent granted to kafka as a produce
    # Produce data by selecting random values from these lists.
    topic = "test"
    user_ids = ['eabara', 'jsmith', 'sgarcia', 'jbernard', 'htanaka', 'awalther']
    products = ['book', 'alarm clock', 't-shirts', 'gift card', 'batteries']
    
    
    count = 0
    for _ in range(10):
        user_id = choice(user_ids)
        product = choice(products)
        producer.produce(topic, product, user_id, callback=delivery_callback)
        count += 1

        # Trigger any outstanding delivery report callbacks.
        producer.poll(0)

    # Block until the messages are delivered.
    producer.flush()
    
    return {"this one works": "hi"}

# def lets_see():
#     running = True
#     try:
#         consumer.subscribe(['test'])
#         while running:
#             msg = consumer.poll(timeout=1.0)
#             if msg is None: print("waiting...")
            
#             elif msg.error():
#                 raise KafkaException(msg.error())
#             else:
#                 print("Consumed event from topic {topic}: key = {key:12} value = {value:12}".format(
# topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))
#     finally:
#         consumer.close()
    
#     return {'executed':'true'}

# @app.on_event("startup")
# def start_consumer():
#     thread = threading.Thread(target=lets_see, daemon=True)
#     thread.start()
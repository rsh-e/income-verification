import uuid
from fastapi import FastAPI
from confluent_kafka import Producer, Consumer, KafkaException, KafkaError
from random import choice


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

# @app.get("/payroll/{user_id}")
# async def payroll(user_id: uuid):
#     consent_granted()
    # Consume from Verification Events topic
    # Return payroll facts
#     {
#   "pagination": {
#     "offset": 75,
#     "limit": 25,
#     "count": 14,
#     "total_count": 89
#   },
#   "payroll_submissions": [
#     {
#       "id": "95a0e70b-fe02-4f47-aef9-2efff279df71",
#       "account_id": "674744df-9626-47ef-ae2b-4a491be136b5",
#       "entry_id": "be770ba4-1362-46cd-8c1c-2330ce3a8b69",
#       "created_at": "2019-05-17T00:00:00.000Z",
#       "identity_information": {
#         "name": "John Smith",
#         "date_of_birth": "2019-05-17T00:00:00.000Z",
#         "address": {
#           "street": "123 Main Street",
#           "county": "Greater London",
#           "city": "London",
#           "post_code": "SW1A 1AA",
#           "country": "United Kingdom"
#         },
#         "email": "john.smith@company.com",
#         "phone": 447123456789,
#         "NI_number": "AB123456C"
#       },
#       "employment_information": {
#         "employer_name": "Acme Ltd",
#         "role": "Software Engineer",
#         "type": "Full-time",
#         "status": "active",
#         "start_date": "2019-05-17T00:00:00.000Z",
#         "leave_date": "2019-05-17T00:00:00.000Z"
#       },
#       "income_information": {
#         "pay_date": "2023-05-27T00:00:00.000Z",
#         "pay_interval_start": "2023-05-01T00:00:00.000Z",
#         "pay_interval_end": "2023-05-31T00:00:00.000Z",
#         "pay_frequency": "Monthly",
#         "earnings": {
#           "gross_pay": 3500,
#           "net_pay": 2500,
#           "base_salary": 3000,
#           "bonus": 500
#         },
#         "deductions": {
#           "income_tax": 500,
#           "employee_ni": 200,
#           "employee_pension": 300,
#           "total_deductions": 1000
#         }
#       },
#       "document_id": "95a0e70b-fe02-4f47-aef9-2efff279df71",
#       "document_external_id": "payslip123456",
#       "document_filename": "file1-payslip.pdf",
#       "fraud_risk": "Low"
#     }
#   ]
# }


@app.get("/consent-granted")
async def consent_granted():
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

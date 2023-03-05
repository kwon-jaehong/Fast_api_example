from fastapi import FastAPI
import asyncio
from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
import json
import uvicorn

import asyncio

from pydantic import BaseModel

class Message(BaseModel):
    message : str

# env Variable
KAFKA_BOOTSTRAP_SERVERS= "localhost:9092"
KAFKA_TOPIC="kafka"
KAFKA_CONSUMER_GROUP="group-id"
loop = asyncio.get_event_loop()


app = FastAPI()

@app.get('/')
async def Home():
    return "welcome home"

# app.include_router(router.route)


@app.post('/create_message')
async def send(message: Message):
    producer = AIOKafkaProducer(loop=loop,bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
    await producer.start()
    try:
        print(f'Sendding message with value: {message}')
        value_json = json.dumps(message.__dict__).encode('utf-8')
        # value_json = b'{"message": "string"}'
        await producer.send_and_wait(topic=KAFKA_TOPIC, value=value_json)
    finally:
        await producer.stop()

async def consume():
    consumer = AIOKafkaConsumer(KAFKA_TOPIC, loop=loop,
                                bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
    await consumer.start()
    try:
        async for msg in consumer:
            print(f'Consumer msg: {msg}')
    finally:
        await consumer.stop()
    print("노래 끗")
        
asyncio.create_task(consume())

# if __name__ == "__main__":
#     uvicorn.run(app,host="0.0.0.0",port=32220)
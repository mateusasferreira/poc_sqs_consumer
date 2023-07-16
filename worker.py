import json
import os
from sqs_queue import Queue

from dotenv import load_dotenv

load_dotenv()

def process_message(payload):
    payload = json.loads(payload['Body'])
    message = payload["message"]

    print(f"New message arrived: {message}")

if __name__ == "__main__":

    print("Worker started. Waiting for messages...")

    while True:
        queue = Queue(os.environ.get('QUEUE_URL'))

        response = queue.consume()

        if "Messages" in response:
            for message in response["Messages"]:
                try:
                    process_message(message)
                except Exception as error:
                    queue.delay(message['ReceiptHandle'], 60)

                    print(f"Error while processing message: {error}")
                else:
                    queue.delete(message['ReceiptHandle'])


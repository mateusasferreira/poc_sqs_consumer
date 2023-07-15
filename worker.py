import json
import consumer

def process_message(payload):
    payload = json.loads(payload['Body'])
    message = payload["message"]
    print(f"New message arrived: {message}")

if __name__ == "__main__":

    print("Worker started. Waiting for messages...")

    while True:
        response = consumer.consume()

        if "Messages" in response:
            for message in response["Messages"]:
                process_message(message)
import boto3
import json
import os

from dotenv import load_dotenv
from credentials import get_credentials

load_dotenv()

def process_message(payload):
    payload = json.loads(payload['Body'])
    message = payload["message"]
    print(f"New message arrived: {message}")

def consume():
    credentials = get_credentials()

    client = boto3.client(
        'sqs',
        aws_access_key_id=credentials["access_key"],
        aws_secret_access_key=credentials["secret_key"],
        aws_session_token=credentials["session_token"]
    )

    response = client.receive_message(
        QueueUrl=os.environ.get('QUEUE_URL'),
        MaxNumberOfMessages=10
    )

    if ("Messages" in response):
        for message in response['Messages']:
            process_message(message)

import boto3
import json
import os

from dotenv import load_dotenv
from credentials import get_credentials

load_dotenv()

def publish(message):
    credentials = get_credentials()

    client = boto3.client(
        'sqs',
        aws_access_key_id=credentials["access_key"],
        aws_secret_access_key=credentials["secret_key"],
        aws_session_token=credentials["session_token"]
    )

    response = client.send_message(
        QueueUrl=os.environ.get('QUEUE_URL'),
        MessageBody=json.dumps({
            "message": message
        }),
    )

    return response
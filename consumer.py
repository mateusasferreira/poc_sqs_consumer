import boto3
import json
import os

from dotenv import load_dotenv
from credentials import get_credentials

load_dotenv()

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

    return response

def delete(receipt_handle):
    credentials = get_credentials()

    client = boto3.client(
        'sqs',
        aws_access_key_id=credentials["access_key"],
        aws_secret_access_key=credentials["secret_key"],
        aws_session_token=credentials["session_token"]
    )

    response = client.delete_message(
        QueueUrl=os.environ.get('QUEUE_URL'),
        ReceiptHandle=receipt_handle
    )

    return response
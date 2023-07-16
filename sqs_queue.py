
import json
import boto3

class Queue:

    def __init__(self, queue_url: str):
        credentials = self.__get_credentials()

        self.queue_url = queue_url
        self.client = boto3.client(
            'sqs',
            aws_access_key_id=credentials["access_key"],
            aws_secret_access_key=credentials["secret_key"],
            aws_session_token=credentials["session_token"]
        )


    def __get_credentials(self):
        client = boto3.client('sts')

        response = client.get_session_token()

        credentials = response["Credentials"]

        return {
            "access_key": credentials["AccessKeyId"],
            "secret_key": credentials["SecretAccessKey"],
            "session_token": credentials["SessionToken"]
        }

    def publish(self, payload: dict):
        response = self.client.send_message(
            QueueUrl=self.queue_url,
            MessageBody=json.dumps(payload),
        )

        return response

    def consume(self):
        response = self.client.receive_message(
            QueueUrl=self.queue_url,
            MaxNumberOfMessages=10
        )

        return response

    def delete(self, receipt_handle):
        response = self.client.delete_message(
            QueueUrl=self.queue_url,
            ReceiptHandle=receipt_handle
        )

        return response
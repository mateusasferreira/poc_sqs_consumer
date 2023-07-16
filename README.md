# About

This is a Proof-of-concept (POC) on how to build a simple consumer for an SQS queue with python and boto3

# Requirements:

- Python (>=3.8)

# Getting Started

Create a .env file:

```
QUEUE_URL=<your-sqs-queue-url>

AWS_ACCESS_KEY=<your-aws-access-key>
AWS_SECRET_KEY=<your-aws-secret-key>

```

Create a virtual env:

```shell
python3 -m venv venv
```

Activate the virtual env:

```shell
source venv/bin/activate
```

Install requirements:

```shell
pip install -r requirements.txt
```

Run the worker:

```
python3 worker.py
```

You can test the consumer by publishing messages directly from the aws console or programmatically from the SDK. The worker will successfully process messages with the payload format `{"message":"foo"}`. Other formats are a way to test error scenarios such as delaying and sending messages to a dead letter queue.

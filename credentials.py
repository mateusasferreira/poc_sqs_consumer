import boto3


def get_credentials():
    client = boto3.client('sts')

    response = client.get_session_token()

    credentials = response["Credentials"]

    return {
        "access_key": credentials["AccessKeyId"],
        "secret_key": credentials["SecretAccessKey"],
        "session_token": credentials["SessionToken"]
    }
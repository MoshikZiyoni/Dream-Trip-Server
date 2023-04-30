# import json
# import boto3
# import base64
# from botocore.exceptions import ClientError

# def lambda_handler(event, context):
#     secret_name = "openaisecret" 
#     region_name = "eu-north-1"

#     # Create a Secrets Manager client
#     session = boto3.session.Session()
#     client = session.client(
#         service_name='secretsmanager',
#         region_name=region_name
#     )

#     try:
#         secret_value_response = client.get_secret_value(
#             SecretId=secret_name
#         )
#     except ClientError as error:
#         print (error)
#     else:
#         if 'SecretString' in secret_value_response:
#             secret= json.loads(secret_value_response['SecretString'])
#             return secret
#         else:
#             decoded_binary_secret=base64.b64decode(secret_value_response['SecretBinary'])
#             return decoded_binary_secret


# import json
# import boto3
# import base64
# from botocore.exceptions import ClientError

# def lambda_handler(event, context):
#     secret_name = "openaisecret" 
#     region_name = "eu-north-1"

#     # Create a Secrets Manager client
#     session = boto3.session.Session()
#     client = session.client(
#         service_name='secretsmanager',
#         region_name=region_name
#     )

#     try:
#         secret_value_response = client.get_secret_value(
#             SecretId=secret_name
#         )
#     except ClientError as error:
#         print (error)
#     else:
#         if 'SecretString' in secret_value_response:
#             secret= json.loads(secret_value_response['SecretString'])
#             return {'API_KEY': secret['API_KEY']}
#         else:
#             decoded_binary_secret=base64.b64decode(secret_value_response['SecretBinary'])
#             return {'API_KEY': decoded_binary_secret['API_KEY']}

import boto3
from botocore.exceptions import ClientError

def get_secret():
    secret_name = "openaisecret"
    region_name = "eu-north-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['API_KEY']

    return secret
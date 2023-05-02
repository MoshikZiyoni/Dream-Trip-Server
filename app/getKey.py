import boto3

def create_api_gateway():
    lambda_client = boto3.client('lambda')
    apigateway_client = boto3.client('apigateway')

    # Create a new API Gateway REST API
    api_id = apigateway_client.create_rest_api(name='secretMangerLambda-API')['id']

    # Create a new resource under the root resource
    root_resource_id = apigateway_client.get_resources(restApiId=api_id)['items'][0]['id']
    resource_id = apigateway_client.create_resource(restApiId=api_id, parentId=root_resource_id, pathPart='{proxy+}')['id']

    # Create a new method for the resource
    apigateway_client.put_method(restApiId=api_id, resourceId=resource_id, httpMethod='ANY', authorizationType='NONE')

    # Set up integration between the method and your Lambda function
    lambda_arn = lambda_client.get_function(FunctionName='secretMangerLambda')['Configuration']['FunctionArn']
    apigateway_client.put_integration(restApiId=api_id, resourceId=resource_id, httpMethod='ANY', integrationHttpMethod='POST', type='AWS_PROXY', uri=lambda_arn)

    # Set up a method response
    apigateway_client.put_method_response(restApiId=api_id, resourceId=resource_id, httpMethod='ANY', statusCode='200')

    # Set up an integration response
    apigateway_client.put_integration_response(restApiId=api_id, resourceId=resource_id, httpMethod='ANY', statusCode='200', selectionPattern='.*')

    # Deploy the API Gateway to a stage
    deployment_id = apigateway_client.create_deployment(restApiId=api_id, stageName='prod')['id']

    # Get the URL of the deployed API Gateway
    url = f'https://4ogl36nnee.execute-api.eu-north-1.amazonaws.com/default'

    return url

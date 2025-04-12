import boto3
import json
import os
import logging

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ.get('DYNAMODB_TABLE'))
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        logger.info(f"Processing file: {key} from bucket: {bucket}")

        s3 = boto3.client('s3')
        response = s3.get_object(Bucket=bucket, Key=key)
        content = response['Body'].read().decode('utf-8')

        item = {
            'FileName': key,
            'Data': content
        }
        table.put_item(Item=item)
        logger.info(f"Data inserted into DynamoDB: {item}")

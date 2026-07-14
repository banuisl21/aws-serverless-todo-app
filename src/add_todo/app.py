import json
import uuid
import os
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    body = json.loads(event['body'])
    
    item = {
        'id': str(uuid.uuid4()),
        'task': body.get('task', ''),
        'status': 'pending'
    }
    
    table.put_item(Item=item)
    
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }

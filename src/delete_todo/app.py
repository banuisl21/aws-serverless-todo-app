import json
import os
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    todo_id = event['pathParameters']['id']
    
    table.delete_item(
        Key={'id': todo_id}
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Todo item deleted'})
    }

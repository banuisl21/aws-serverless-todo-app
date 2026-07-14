import json
import os
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    todo_id = event['pathParameters']['id']
    body = json.loads(event['body'])
    
    update_expression = "SET "
    expression_values = {}
    
    if 'task' in body:
        update_expression += "task = :task, "
        expression_values[':task'] = body['task']
        
    if 'status' in body:
        update_expression += "status = :status, "
        expression_values[':status'] = body['status']
    
    update_expression = update_expression.rstrip(", ")
    
    table.update_item(
        Key={'id': todo_id},
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_values
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Todo item updated'})
    }

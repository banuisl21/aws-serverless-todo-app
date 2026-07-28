import json
import boto3
import os
import uuid
dynamodb= boto3.resource('dynamodb')

table_name = os.environ.get('TABLE_NAME')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    """
    Entry point for the AWS Lambda function.
    Receives the request from API Gateway and returns a JSON response.
    """
    method = event["httpMethod"]

    if method == "POST":

        body = json.loads(event["body"])

        task = {
            "taskId": str(uuid.uuid4()),
            "title": body["title"],
            "status": body.get("status", "Pending")
        }

        table.put_item(Item=task)
    
        return {
          "statusCode": 201,
          "body": json.dumps({
             "message": "Task created successfully!",
             "task": task
        })
        }
    # ---------- GET ----------
    elif method == "GET":

        response = table.scan()

        return {
            "statusCode": 200,
            "body": json.dumps(response["Items"])
        }
    # ---------- PUT ----------
    elif method == "PUT":

        task_id = event["pathParameters"]["taskId"]

        body = json.loads(event["body"])

        table.update_item(
            Key={
                "taskId": task_id
            },
            UpdateExpression="SET title = :t, #s = :s",
            ExpressionAttributeNames={
                "#s": "status"
            },
            ExpressionAttributeValues={
                ":t": body["title"],
                ":s": body["status"]
            }
        )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Task updated successfully!"
            })
        }
    # ---------- DELETE ----------
    elif method == "DELETE":

        task_id = event["pathParameters"]["taskId"]

        table.delete_item(
            Key={
                "taskId": task_id
            }
        )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Task deleted successfully!"
            })
        }
    
    return {
        "statusCode": 400,
        "body": json.dumps({
            "message": "Unsupported HTTP Method"
        })
    }
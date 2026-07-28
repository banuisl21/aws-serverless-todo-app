import json
import os
import uuid
import boto3

# Initialize DynamoDB
dynamodb = boto3.resource("dynamodb")
table_name = os.environ.get("TABLE_NAME")
table = dynamodb.Table(table_name)


def lambda_handler(event, context):
    """
    AWS Lambda entry point for TaskFlow CRUD operations.
    """

    try:
        method = event.get("httpMethod")

        # ==========================
        # CREATE TASK (POST)
        # ==========================
        if method == "POST":

            body = json.loads(event.get("body", "{}"))

            title = body.get("title")

            if not title:
                return {
                    "statusCode": 400,
                    "body": json.dumps({
                        "message": "Title is required."
                    })
                }

            task = {
                "taskId": str(uuid.uuid4()),
                "title": title,
                "status": body.get("status", "Pending")
            }

            table.put_item(Item=task)

            return {
                "statusCode": 201,
                "body": json.dumps({
                    "message": "Task created successfully.",
                    "task": task
                })
            }

        # ==========================
        # GET ALL TASKS
        # ==========================
        elif method == "GET":

            response = table.scan()

            return {
                "statusCode": 200,
                "body": json.dumps(response.get("Items", []))
            }

        # ==========================
        # UPDATE TASK
        # ==========================
        elif method == "PUT":

            task_id = event["pathParameters"]["taskId"]

            body = json.loads(event.get("body", "{}"))

            title = body.get("title")
            status = body.get("status")

            if not title or not status:
                return {
                    "statusCode": 400,
                    "body": json.dumps({
                        "message": "Both title and status are required."
                    })
                }

            response = table.update_item(
                Key={
                    "taskId": task_id
                },
                UpdateExpression="SET title = :t, #s = :s",
                ExpressionAttributeNames={
                    "#s": "status"
                },
                ExpressionAttributeValues={
                    ":t": title,
                    ":s": status
                },
                ReturnValues="UPDATED_NEW"
            )

            return {
                "statusCode": 200,
                "body": json.dumps({
                    "message": "Task updated successfully.",
                    "updatedAttributes": response.get("Attributes")
                })
            }

        # ==========================
        # DELETE TASK
        # ==========================
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
                    "message": "Task deleted successfully."
                })
            }

        # ==========================
        # INVALID METHOD
        # ==========================
        else:
            return {
                "statusCode": 405,
                "body": json.dumps({
                    "message": "Method Not Allowed."
                })
            }

    # Invalid JSON
    except json.JSONDecodeError:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "Invalid JSON format."
            })
        }

    # Missing keys
    except KeyError as e:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": f"Missing required field: {str(e)}"
            })
        }

    # Any unexpected error
    except Exception as e:
        print(f"Error: {str(e)}")

        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "Internal Server Error",
                "error": str(e)
            })
        }
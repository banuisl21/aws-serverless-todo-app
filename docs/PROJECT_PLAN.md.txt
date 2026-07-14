# TaskFlow - Serverless Task Management API

## Project Goal

Build a production-style serverless REST API using AWS Lambda, API Gateway, DynamoDB and AWS SAM.

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /tasks | Create a new task |
| GET | /tasks | Get all tasks |
| GET | /tasks/{id} | Get a task by ID |
| PUT | /tasks/{id} | Update a task |
| DELETE | /tasks/{id} | Delete a task |

---

## AWS Services

- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- AWS CloudFormation (SAM)
- Amazon CloudWatch
- IAM

---

## Deployment

AWS SAM

---

## Future Enhancements

- Authentication using Cognito
- Pagination
- Search Tasks
- Filter by Status
- File Attachments
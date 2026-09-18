# aws-serverless-todo-app
AWS serverless to-do application using Lambda
# 📝 AWS Serverless Todo App | Lambda + API Gateway + DynamoDB + Cloudwatch

A fully serverless todo application built using AWS services with CRUD functionality.

## 🔥 Features
- **Add, view, update, and delete tasks** via REST API
- **JWT-based authentication** (optional - if implemented)
- **Auto-scaling & cost-efficient** (pay-per-use pricing)
- **Infrastructure as Code** (deployed using AWS SAM/Terraform)

## 🛠 Tech Stack
| AWS Service      | Purpose                          |
|------------------|----------------------------------|
| AWS Lambda       | Backend logic (Python/Node.js)   |
| API Gateway      | REST API endpoint                |
| DynamoDB         | Database for storing tasks       |
| IAM              | Security permissions             |
| CloudWatch       | Logging & monitoring             |

## 📦 Prerequisites
- AWS account (Free Tier eligible)
- AWS CLI configured (`aws configure`)
- Python 3.x/Node.js (if using Lambda)

## 🚀 Deployment Steps

```bash
## Deployment

The application is deployed using **AWS SAM (Serverless Application Model)**. AWS resources are defined in `template.yaml` and provisioned through AWS CloudFormation.

### 1. Clone the repository

```bash
git clone <https://github.com/banuisl21/aws-serverless-todo-app/>
cd aws-serverless-todo-app
```

### 2. Validate the SAM template

```bash
sam validate
```

### 3. Build the application

```bash
sam build
```

### 4. Deploy to AWS

For the first deployment:

```bash
sam deploy --guided
```

During the guided deployment, provide the required stack name, AWS Region, and IAM permissions. Save the deployment configuration to `samconfig.toml` for subsequent deployments.

For future deployments:

```bash
sam build
sam deploy
```

### 5. Access the API

After deployment, the API Gateway endpoint is displayed in the SAM/CloudFormation outputs.

Use the endpoint with the `/tasks` resource to interact with the application:

```text
https://<api-id>.execute-api.<region>.amazonaws.com/Prod/tasks
```

The API can be tested using Postman.

### 6. Remove the deployment

To delete the CloudFormation stack:

```bash
sam delete --stack-name <stack-name>
```
7. Monitoring and Troubleshooting

TaskFlow uses Amazon CloudWatch to monitor Lambda execution and detect errors.

7.1 CloudWatch Logs

Lambda execution logs are available in:

/aws/lambda/TaskFlowFunction

These logs can be viewed from:

AWS Console → CloudWatch → Logs → Log groups → TaskFlowFunction

The logs were used to verify Lambda execution and investigate errors during testing.

7.2 Lambda Error Alarm

TaskFlow includes a CloudWatch alarm that monitors the Lambda Errors metric.

TaskFlowFunction
      │
      ▼
CloudWatch Errors Metric
      │
      ▼
TaskFlow-Lambda-Errors

The alarm is defined as an AWS resource in template.yaml:

TaskFlowLambdaErrorAlarm:
  Type: AWS::CloudWatch::Alarm

The alarm is configured to detect Lambda execution errors.

7.3 Monitoring Verification

The monitoring setup was verified by intentionally generating a controlled Lambda error.

The error was:

Triggered through the deployed API.
Recorded in the Lambda CloudWatch log stream.
Reflected in the Lambda Errors metric.
Used to verify the CloudWatch alarm configuration.

After verification, the temporary test error was removed from the application code. The application was rebuilt and redeployed, and a normal TaskFlow API request was successfully processed and stored in DynamoDB.

7.4 Basic Troubleshooting

For an API failure, CloudWatch Logs can be checked first to identify Lambda execution errors.

The main application flow is:

API Gateway
     ↓
Lambda
     ↓
DynamoDB

CloudWatch Logs help identify where the Lambda execution failed before checking the corresponding API or DynamoDB configuration.

8. Project Structure

The project is organized to keep the AWS SAM configuration separate from the Lambda application code.

TaskFlow/
│
├── src/
│   └── app.py
│
├── template.yaml
├── samconfig.toml
├── requirements.txt
├── README.md
└── events/

File / Directory	      Purpose
src/app.py          	Contains the Lambda function and TaskFlow CRUD logic
template.yaml       	Defines the AWS SAM resources and configuration
samconfig.toml       	Stores SAM deployment configuration
requirements.txt    	Contains Python dependencies used by the application
events/             	Contains sample event payloads used during local testing
README.md            	Project documentation, setup, deployment, API usage, and troubleshooting

The main application flow is:
Client / Postman
       │
       ▼
API Gateway
       │
       ▼
AWS Lambda
(TaskFlowFunction)
       │
       ▼
DynamoDB
(TaskFlowTable)
       │
       ▼
CloudWatch Logs
9. API Endpoints


API Summary
Method	Endpoint	           Operation
POST	  /tasks	           Create a task
GET   	/tasks	           Retrieve all tasks
PUT	  /tasks/{taskId}	     Update a task
DELETE	/tasks/{taskId}	   Delete a task

Future Enhancements:
Add authentication and authorization using Amazon cognito
Add CI/CD using GitHub actions and AWS SAM.

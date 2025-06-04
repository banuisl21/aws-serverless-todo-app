# aws-serverless-todo-app
AWS serverless to-do application using Lambda
# 📝 AWS Serverless Todo App | Lambda + API Gateway + DynamoDB

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

### Option 1: AWS SAM
```bash
# Clone this repository
git clone https://github.com/yourusername/aws-serverless-todo.git
cd aws-serverless-todo

# Deploy
sam build
sam deploy --guided

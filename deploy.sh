#!/bin/bash

AWS_REGION="us-east-1"
AWS_ACCOUNT_ID="123456789012"  # Replace with your actual AWS account ID
REPO_NAME="s3-to-rds-or-glue"
IMAGE_TAG="latest"

# Authenticate Docker with ECR
echo "Authenticating Docker with AWS ECR..."
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

# Build the Docker image
echo "Building the Docker image..."
docker build -t $REPO_NAME .

# Tag the Docker image
echo "Tagging the Docker image..."
docker tag $REPO_NAME:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO_NAME:$IMAGE_TAG

# Push the Docker image to ECR
echo "Pushing the Docker image to AWS ECR..."
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO_NAME:$IMAGE_TAG

echo "Deployment complete!"
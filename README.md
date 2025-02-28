# AWS Incident Response Automation

## Overview
This project automates IAM security responses using AWS Lambda, 
CloudWatch, and CloudTrail.
If an IAM user is created, Lambda automatically disables the user and 
applies a deny-all policy.

## How It Works
- CloudTrail logs IAM events
- CloudWatch detects `CreateUser` events
- Lambda disables the IAM user
- An SNS notification can be sent (optional)

## Deployment
- Deploy Lambda function in AWS Console
- Attach IAM permissions to allow user modification
- Configure CloudWatch rule to detect IAM user creation

## Author
- Yassin Hussein


# AWS Incident Response Automation Project

## Overview
Pretty much for this project I automated IAM security responses using AWS Lambda, 
CloudWatch, and CloudTrail.
If an IAM user is created, Lambda automatically disables the user and 
applies a deny-all policy... Zero trust Policy!

## How It Works
- CloudTrail logs IAM events
- CloudWatch detects `CreateUser` events
- Lambda disables the IAM user
- An SNS notification can be sent (optional)

## Deployment
- Deploy Lambda function in AWS Console
- Attach IAM permissions to allow user modification
- Configure CloudWatch rule to detect IAM user creation

## Cloud Guru
- Yassin Hussein


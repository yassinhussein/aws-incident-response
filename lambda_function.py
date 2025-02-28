import json
import boto3
from botocore.exceptions import ClientError

iam = boto3.client('iam')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))

    try:
        # Extract username from CloudWatch Event
        user_name = event['detail']['requestParameters']['userName']
        
        # Check if user has a login profile before updating
        try:
            iam.get_login_profile(UserName=user_name)
            iam.update_login_profile(
                UserName=user_name,
                PasswordResetRequired=True
            )
            print(f"User {user_name} login disabled.")
        except ClientError as e:
            if e.response['Error']['Code'] == 'NoSuchEntity':
                print(f"User {user_name} does not have a login profile. 
Skipping login disable step.")
        
        # Attach a policy to deny all actions (extra security)
        deny_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Deny",
                    "Action": "*",
                    "Resource": f"arn:aws:iam::*:user/{user_name}"
                }
            ]
        }
        
        iam.put_user_policy(
            UserName=user_name,
            PolicyName="DenyAllPolicy",
            PolicyDocument=json.dumps(deny_policy)
        )

        print(f"User {user_name} disabled and denied all permissions.")

        return {
            'statusCode': 200,
            'body': json.dumps(f"User {user_name} has been disabled")
        }

    except Exception as e:
        print(f"Error disabling user: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }


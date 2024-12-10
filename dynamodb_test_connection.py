import os
import django
from django.conf import settings
from boto3 import client

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project1.settings') 
django.setup()

def test_dynamodb_connection():
    # Initialize DynamoDB client
    dynamodb = client(
        'dynamodb',
        region_name=settings.DYNAMODB_SETTINGS['AWS_REGION'],
        aws_access_key_id=settings.DYNAMODB_SETTINGS['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=settings.DYNAMODB_SETTINGS['AWS_SECRET_ACCESS_KEY'],
    )

    # Test listing tables
    try:
        response = dynamodb.list_tables()
        print(f"DynamoDB tables: {response['TableNames']}")
    except Exception as e:
        print(f"Error connecting to DynamoDB: {e}")

if __name__ == "__main__":
    test_dynamodb_connection()

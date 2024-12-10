from django.apps import AppConfig
import boto3
from django.conf import settings

class DonutsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Donuts'

    def ready(self):
        """
        Initialize DynamoDB connection when the app starts.
        """
        self.initialize_dynamodb()

    @staticmethod
    def initialize_dynamodb():
        """
        Sets up DynamoDB client using boto3.
        """
        try:
            # Initialize DynamoDB client
            dynamodb = boto3.resource(
                'dynamodb',
                region_name=settings.DYNAMODB_SETTINGS['AWS_REGION'],
                aws_access_key_id=settings.DYNAMODB_SETTINGS['AWS_ACCESS_KEY_ID'],
                aws_secret_access_key=settings.DYNAMODB_SETTINGS['AWS_SECRET_ACCESS_KEY']
            )
            print("DynamoDB initialized successfully.")

        except Exception as e:
            print(f"Error initializing DynamoDB: {e}")

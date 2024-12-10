from django.conf import settings
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

# Access settings for DynamoDB
dynamodb_settings = settings.DYNAMODB_SETTINGS

class Image(Model):
    """
    Represents the DynamoDB table for storing image metadata.
    """
    class Meta:
        table_name = "images"
        region = dynamodb_settings['AWS_REGION']
        aws_access_key_id = dynamodb_settings['AWS_ACCESS_KEY_ID']
        aws_secret_access_key = dynamodb_settings['AWS_SECRET_ACCESS_KEY']

    image_id = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute()
    price = UnicodeAttribute()
    url = UnicodeAttribute()

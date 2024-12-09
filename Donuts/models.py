from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

class Image(Model):
    """
    Represents the DynamoDB table for storing image metadata.
    """
    class Meta:
        table_name = "images"  # Corrected table name
        region = "us-west-2"  # Update with your AWS region

    image_id = UnicodeAttribute(hash_key=True)  # Corrected attribute name
    name = UnicodeAttribute()
    price = UnicodeAttribute()
    url = UnicodeAttribute()

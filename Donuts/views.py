from django.shortcuts import render
from botocore.exceptions import BotoCoreError, ClientError  # Catch specific DynamoDB exceptions
from .models import Image

def index(request):
    """
    Fetch all image objects from the DynamoDB table and render them on the index page.
    """
    try:
        # Attempt to fetch all images from the DynamoDB table
        images = list(Image.scan())
        print(f"Successfully fetched {len(images)} images.")
    except (BotoCoreError, ClientError) as e:
        # Handle AWS-specific errors
        print(f"AWS error while fetching images: {str(e)}")
        images = []
    except Exception as e:
        # Handle any other exceptions
        print(f"Unexpected error: {str(e)}")
        images = []

    return render(request, 'index.html', {'images': images})

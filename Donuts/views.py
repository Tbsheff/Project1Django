from django.shortcuts import render
from .models import Image

def index(request):
    """
    Fetch all image objects from the DynamoDB table and render them on the index page.
    """
    try:
        # Fetch all items from the DynamoDB table
        images = list(Image.scan())  # `scan()` retrieves all items in the table
    except Exception as e:
        print(f"Error fetching images: {e}")
        images = []  # Fallback to an empty list if an error occurs

    # Render the images in the index template
    return render(request, 'index.html', {'images': images})

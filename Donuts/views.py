
# views.py

from django.shortcuts import render
from .models import Flavor

# def home(request):
#     return render(request, "index.html")

def index(request):
    # Fetch all flavor objects from the database
    flavors = Flavor.objects.all()

    # Debugging: print to console to verify data retrieval
    print(flavors)  # This should output something like <QuerySet [<Flavor: Glazed Doughnut>, ...]>
    
    return render(request, 'index.html', {'flavors': flavors})



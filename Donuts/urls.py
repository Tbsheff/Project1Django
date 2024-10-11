# from django.urls import path
# from .views import  home

# urlpatterns = [
#     path("", home, name="home"),
# ]

from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),  # Home page points to index view
]

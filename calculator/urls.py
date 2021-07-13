from django.urls import path
from .views import ingredients_views

urlpatterns = [
    path("<ingredient>/", ingredients_views)
]
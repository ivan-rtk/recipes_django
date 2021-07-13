from django.urls import path, include
from calculator.views import ingredients_views

urlpatterns = [
    path('', include('calculator.urls'))
]

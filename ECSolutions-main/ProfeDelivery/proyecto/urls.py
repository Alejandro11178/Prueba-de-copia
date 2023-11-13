from django.urls import path
from .views import Home, registro

urlpatterns = [
    path('', Home.as_view(), name = 'index'),
    path('registro/', registro, name='registro'),
    
]

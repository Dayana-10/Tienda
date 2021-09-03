from django.urls import path
from .views import *


urlpatterns = [
    path('', Tienda, name='Tienda'),
    path('Dulces/', Dulces, name='Dulces'),
]

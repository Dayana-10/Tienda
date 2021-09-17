from django.urls import path
from .views import *


urlpatterns = [
    path('', Tienda, name='Tienda'),
    path('', shoes, name='shoes'),
    path('', contact, name='contact'),
    path('', collection, name='collection'),
    path('', racingboots, name='racingboots'),

]

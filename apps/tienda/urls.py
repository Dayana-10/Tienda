from django.urls import path
from .views import *


urlpatterns = [
    path('', Tienda, name='Tienda'),
    path('shoes/', shoes, name='shoes'),
    path('contact/', contact, name='contact'),
    path('collection/', collection, name='collection'),
    path('racingboots/', racingboots, name='racingboots'),

]

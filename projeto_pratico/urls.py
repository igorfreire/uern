from django.urls import path
from app.views import ola, list_pizzas

urlpatterns = [
    path('', ola, name='ola'),
    path('pizzas/', list_pizzas, name='list_pizzas')
]
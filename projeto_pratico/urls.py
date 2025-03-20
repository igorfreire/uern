from django.urls import path
from app import views

urlpatterns = [
    path('pizzas/', views.list_pizzas, name='list_pizzas')
]
from django.urls import path
from .consumers import FoodPaidConsumer
websocket_urlpatterns =[
    path('ws/', FoodPaidConsumer.as_asgi()),    
] 
from django.urls import path
from .consumers import OrderConsumer

websocket_urlpatterns = [
    path('ws/service/', OrderConsumer.as_asgi()),
]

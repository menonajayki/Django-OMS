"""
ASGI config for order_management_system project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import orders.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'order_management_system.settings')

# Get the default Django ASGI application
django_asgi_app = get_asgi_application()

# Define the WebSocket URL routing from orders.routing
websocket_urlpatterns = orders.routing.websocket_urlpatterns

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
        orders.routing.websocket_urlpatterns
    ),
})
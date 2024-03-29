import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import orders.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'order_management_system.settings')

# ASGI application
django_asgi_app = get_asgi_application()

# WebSocket URL routing from orders.routing
websocket_urlpatterns = orders.routing.websocket_urlpatterns

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
        orders.routing.websocket_urlpatterns
    ),
})
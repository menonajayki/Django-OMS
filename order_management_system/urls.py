from django.contrib import admin
from django.urls import path, include
from orders import routing
from .views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('users/', include('users.urls')),
    path('orders/', include('orders.urls')),
    path('ws/', include(routing.websocket_urlpatterns)),
]

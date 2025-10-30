import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from chat import routing  # chat/routing.py import করা হলো

# Django settings module সেট করা
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChatApp.settings')

# Django ASGI application
django_asgi_app = get_asgi_application()

# Main ASGI application (both HTTP & WebSocket supported)
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})

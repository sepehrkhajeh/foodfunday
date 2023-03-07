from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from cart import routing as cart_routing
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hermesfood.settings")



application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            cart_routing.websocket_urlpatterns,
        )
    )
})  
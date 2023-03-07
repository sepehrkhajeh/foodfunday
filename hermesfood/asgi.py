"""
ASGI config for hermesfood project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from cart import routing as cart_routing
from channels.routing import ProtocolTypeRouter,URLRouter
import django
from django.core.asgi import get_asgi_application
from . import settings
settings.configure()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hermesfood.settings')
django.setup(True)


django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    'websocket': AuthMiddlewareStack(
        URLRouter(
            cart_routing.websocket_urlpatterns,

        )
    )
})  
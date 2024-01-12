import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django_asgi_app = get_asgi_application()

# from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter #, URLRouter

application = ProtocolTypeRouter({
    'http': django_asgi_app,
})


    # 'websocket': AuthMiddlewareStack(
    #     URLRouter(
    #         FriendRouting.websocket_urlpatterns + UserRouting.websocket_urlpatterns
    #     )
    # )
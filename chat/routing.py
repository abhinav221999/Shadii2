from django.urls import re_path
from . import consumers


websocket_urlpatterns = [
    re_path(r'chat/$', consumers.ChatRoomConsumer.as_asgi()), # removed ws/ from url
]
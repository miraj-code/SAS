from django.urls import path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'chat-group', views.ChatGroupViewSet)

app_name = 's_chat'

urlpatterns = [
    path('chat-api/', include(router.urls)),
    path('chat/login/', views.user_login, name='login'),
    path('chat/', views.chatindex, name='chatindex'),
    path('chat/<str:room_name>/', views.room, name="room"),
]
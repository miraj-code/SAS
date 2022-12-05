from django.urls import path

from . import views


app_name = "sas_chat_bot"

urlpatterns = [
	path('chat-index/', views.index, name='index'),
    path('chat-bot/', views.bot, name='bot'),
]
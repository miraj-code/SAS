from django.contrib import admin
from s_chat.models import ChatGroup, ChatGroupMessage

admin.site.register(ChatGroup)
admin.site.register(ChatGroupMessage)


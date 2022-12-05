from django.apps import AppConfig


class SChatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 's_chat'
    verbose_name = "Student Chat"
    verbose_name_plural = "Student Chats"
    icon = 'fa fa-comments'

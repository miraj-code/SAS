from django.apps import AppConfig


class AUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'a_user'
    verbose_name = "User"
    verbose_name_plural = "Users"
    icon = 'fa fa-user'

from django.apps import AppConfig


class UsersappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "usersapp"

    def ready(self):
        import usersapp.signals

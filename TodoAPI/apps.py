from django.apps import AppConfig


class TodoapiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "TodoAPI"
    
    def ready(self) :
        import TodoAPI.signals


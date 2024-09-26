from django.apps import AppConfig

class DatasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'datas'

    def ready(self):
        # This ensures the cron job is loaded when the app is ready
        from .cron import PrintSomethingCronJob

from django.apps import AppConfig


class PlanlabConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'PlanLab'

    def ready(self):
        import PlanLab.signals  # Conectando o arquivo de sinais

from django.apps import AppConfig
from importlib import import_module


class DriversConfig(AppConfig):
    name = 'drivers'

    def ready(self):
        import_module("transi.receivers")

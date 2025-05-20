from django.apps import AppConfig
"""Конфигурация приложения api."""


class ApiConfig(AppConfig):
    """Класс конфигурации приложения api."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

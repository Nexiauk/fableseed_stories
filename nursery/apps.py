"""
Configuration for the Nursery app.

Defines the app name and default auto field for models.
"""
from django.apps import AppConfig


class NurseryConfig(AppConfig):
    """
    Configuration class for the 'nursery' app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'nursery'

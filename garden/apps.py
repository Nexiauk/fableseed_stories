"""
Configuration for the 'garden' Django app.

This module defines the GardenConfig class, which specifies the default
auto field and app name. The ready() method imports the signals module
when the app is fully loaded to avoid circular import issues and ensure
signal handlers are registered correctly.
"""

from django.apps import AppConfig


class GardenConfig(AppConfig):
    """
    Configuration class for the 'garden' app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'garden'

    def ready(self):
        """
        Perform initialization tasks when the app is ready.

        Specifically, imports the signals module to register
        signal handlers for the Garden app.
        """
        import garden.signals

from django.apps import AppConfig


class DjStudioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    verbose_name = 'Studio'
    name = 'DJ_Studio'


class DjStudioConfig2(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    verbose_name = 'Django Studio'
    name = 'DJ_Studio'

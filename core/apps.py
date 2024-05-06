from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    # Specify custom AdminConfig
    default_site = "sites.AdminSite"

from django.apps import AppConfig


class UserProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_blogging_app.apps.user_profile'

    def ready(self):
        import django_blogging_app.apps.user_profile.signals

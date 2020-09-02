from django.apps import AppConfig

class ProfilesAppConfig(AppConfig):
    name = 'profiles'
    label = 'profiles'
    verbose_name = 'profiles'

    def ready(self):
        import profiles.signals

default_app_config = 'profiles.ProfilesAppConfig'
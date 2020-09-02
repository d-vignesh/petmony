from django.contrib import admin

from .models import Profile, Cities, States, Countries

admin.site.register(Profile)
admin.site.register(Cities)
admin.site.register(States)
admin.site.register(Countries)

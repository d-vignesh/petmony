from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    image = models.URLField(blank=True)
    locality = models.TextField(blank=True)
    city = models.ForeignKey('Cities', on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey('States', on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey('Countries', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Cities(models.Model):

    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city

class States(models.Model):

    state = models.CharField(max_length=100)

    def __str__(self):
        return self.state 

class Countries(models.Model):

    country = models.CharField(max_length=100)

    def __str__(self):
        return self.country 

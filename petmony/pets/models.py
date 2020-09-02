from django.db import models
from django.conf import settings
from django.utils import timezone

import uuid 

User = settings.AUTH_USER_MODEL

class Pet(models.Model):

    GENDER_CHOICES = (
        ('m', 'male'),
        ('f', 'female')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    breed = models.ForeignKey('Breed', on_delete=models.SET_NULL, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    weight = models.FloatField(null=True)
    height = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    dob = models.DateField()
    bio = models.TextField(blank=True)

    @property
    def age(self):
        return timezone.now().year - self.dob.year

class Category(models.Model):

    category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category


class Breed(models.Model):

    breed = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.breed




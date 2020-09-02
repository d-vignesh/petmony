from rest_framework import serializers

from .models import (Pet, Category, Breed)
from authentication.models import User

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "category"]
        read_only_fields = ["id"]

class BreedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Breed
        fields = ["id", "breed"]
        read_only_fields = ["id"]

class PetRegistrationSerializer(serializers.ModelSerializer): 
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    breed = serializers.PrimaryKeyRelatedField(queryset=Breed.objects.all())

    class Meta:
        model = Pet
        fields = ['id', 'name', 'category', 'breed', 'weight', \
                'height', 'age', 'bio', 'dob']

class PetSerializer(serializers.ModelSerializer):
    locality = serializers.CharField(source="owner.profile.locality")
    city = serializers.CharField(source="owner.profile.city")
    state = serializers.CharField(source="owner.profile.state")
    country = serializers.CharField(source="owner.profile.country")

    class Meta:
        model = Pet
        fileds = ["id", "name", "category", "breed", "weigth", "height",  \
                 "age", "bio", "locality", "city", "state", "country"]

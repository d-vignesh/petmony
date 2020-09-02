from rest_framework import status
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics

from ..models import (Pet, Category, Breed) 
from ..serializers import (
    PetRegistrationSerializer,
    CategorySerializer,
    BreedSerializer,
)
from ..renderers import PetJSONRenderer

class PetRegistrationAPIView(APIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = PetRegistrationSerializer
    renderer_classes = (PetJSONRenderer,)

    def post(self, request):
    
        pet = request.data.get('pet', {})
        print(pet)

        serializer = self.serializer_class(data=pet)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner = request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CategoryListAPIView(generics.ListCreateAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BreedListAPIView(generics.ListCreateAPIView):

    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

class BreedDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
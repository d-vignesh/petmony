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
    PetListSerializer,
    PetSerializer,
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

class PetListAPIView(generics.ListAPIView):

    queryset = Pet.objects.all()
    serializer_class = PetListSerializer

class PetRetrieveUpdateAPIView(APIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = PetSerializer

    def get(self, request, pk, *args, **kwargs):
        qs = Pet.objects.filter(id=pk)
        if not qs.exists():
            return Response({"error": "pet not found"}, status=status.HTTP_404_NOT_FOUND)
        pet = self.serializer_class(qs.first())
        return Response(pet.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        qs = Pet.objects.filter(id=pk)
        if not qs.exists():
            return Response({"error": "pet not found"}, status=status.HTTP_404_NOT_FOUND)
        pet = self.serializer_class(qs.first(), data=request.data, partial=True)
        pet.is_valid(raise_exception=True)
        pet.save()
        return Response(pet.data, status=status.HTTP_200_OK)


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
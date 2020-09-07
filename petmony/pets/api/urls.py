from django.urls import path

from . import views 

urlpatterns = [
    path("register/", views.PetRegistrationAPIView.as_view()),
    path("breed/", views.BreedListAPIView.as_view()),
    path("breed/<int:pk>", views.BreedDetailAPIView.as_view()),
    path("category/", views.CategoryListAPIView.as_view()),
    path("category/<int:pk>", views.CategoryDetailAPIView.as_view()),
    path("", views.PetListAPIView.as_view()),
    path("<str:pk>/", views.PetRetrieveUpdateAPIView.as_view()),
]
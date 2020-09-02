from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserRetrieveUpdateAPIView.as_view()),
    path('register/', views.UserRegistrationAPIView.as_view()),
    path('login/', views.UserLoginAPIView.as_view()),
]
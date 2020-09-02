from django.urls import path

from .views import ProfileRetrieveAPIView

urlpatterns = [
    path('<str:username>', ProfileRetrieveAPIView.as_view()),
]
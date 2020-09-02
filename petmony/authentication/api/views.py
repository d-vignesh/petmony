from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView

from ..serializers import (
    UserRegistrationSerializer, UserLoginSerializer, UserSerializer
)
from ..renderers import UserJSONRenderer

class UserRegistrationAPIView(APIView):

    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer
    renderer_classes = (UserJSONRenderer,)

    def post(self, request):

        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserLoginAPIView(APIView):

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer
    renderer_classes = (UserJSONRenderer,)

    def post(self, request):

        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer 
    renderer_classes = (UserJSONRenderer,)

    def retrieve(self, request, *args, **kwargs):
        
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):

        request_data = request.data.get('user', {})

        user_data = {
            'username': request_data.get('username', request.user.username),
            'email': request_data.get('email', request.user.email),
            'first_name': request_data.get('first_name', request.user.first_name),
            'last_name': request_data.get('last_name', request.user.last_name),
            'password': request_data.get('password', request.user.password),
            'profile': {
                'bio': request_data.get('bio', request.user.profile.bio),
                'image': request_data.get('image', request.user.profile.image),
                'locality': request_data.get('locality', request.user.profile.locality),
                'city': request_data.get('city', request.user.profile.city),
                'state': request_data.get('state', request.user.profile.state),
                'country': request_data.get('country', request.user.profile.country)
            }
        }
        serializer = self.serializer_class(request.user, data=user_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)




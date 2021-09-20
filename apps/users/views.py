from datetime import datetime

from django.contrib.auth import logout, authenticate, login
from django.contrib.sessions.models import Session
from rest_framework import status, views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.users.serializers import UserSerializer, UserLoginSerializer


class LoginAPIView(views.APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            token = serializer.data['token']

            user = authenticate(username=data['email'], password=data['password'])
            login(request, user)
            new_data = {
                'user': UserSerializer(instance=user).data,
                'token': token
            }
            return Response(new_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(views.APIView):

    def get(self, request):
        if request.user.is_authenticated:
            if request.user.auth_token:
                request.user.auth_token.delete()
            logout(request)
            return Response({'message': 'Sesión cerrada correctamente'}, status=status.HTTP_200_OK)
        return Response({'message': 'Sesión no iniciada'}, status=status.HTTP_400_BAD_REQUEST)

# class UserListView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from apps.users.models import User
from apps.users.serializers import UserSerializer


class LoginView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        token_serializer = self.serializer_class(data=request.data, context={'request': request})
        if token_serializer.is_valid():
            user = token_serializer.validated_data['user']
            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                user_serializer = UserSerializer(user)
                if created:
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data
                    }, status=status.HTTP_201_CREATED)
                else:
                    token.delete()
                    token = Token.objects.create(user=user)
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data
                    }, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Este usuario no puede iniciar sesión'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Nombre de usuario o contraseña incorrectos'}, status=status.HTTP_400_BAD_REQUEST)

# class UserListView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

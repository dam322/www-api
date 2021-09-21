from datetime import datetime

from django.contrib.auth import logout, authenticate, login
from django.contrib.sessions.models import Session
from rest_framework import status, views, generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.users.models import User, Restaurant
from apps.users.serializers import UserSerializer, UserLoginSerializer, SignupSerializer, RestaurantSerializer


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
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if request.user.is_authenticated:
            if request.user.auth_token:
                request.user.auth_token.delete()
            logout(request)
            return Response({'message': 'Sesión cerrada correctamente'}, status=status.HTTP_200_OK)
        return Response({'message': 'Sesión no iniciada'}, status=status.HTTP_400_BAD_REQUEST)


class SignupAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SignupSerializer


class ListEmployeesView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = SignupSerializer

    def get_queryset(self):
        restaurant = Restaurant.objects.get(administrator=self.request.user)
        return restaurant.employees


class AccountAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer


class RestaurantRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = RestaurantSerializer


class CustomPagination(PageNumberPagination):
    max_page_size = 20
    page_size = 20


class RestaurantListCreateAPIView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = RestaurantSerializer
    pagination_class = CustomPagination

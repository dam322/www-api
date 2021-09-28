from django.contrib.auth import logout, authenticate, login
from rest_framework import status, views, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.users.models import User
from apps.users.serializers import UserSerializer, UserLoginSerializer, SignupSerializer


class Login(views.APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            token = serializer.data['token']

            user = authenticate(username=data['email'], password=data['password'])
            login(request, user)
            new_data = UserSerializer(instance=user).data
            new_data['token'] = token
            return Response(new_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Logout(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if request.user.is_authenticated:
            if request.user.auth_token:
                request.user.auth_token.delete()
            logout(request)
            return Response({'message': 'Sesión cerrada correctamente'}, status=status.HTTP_200_OK)
        return Response({'message': 'Sesión no iniciada'}, status=status.HTTP_400_BAD_REQUEST)


class Signup(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SignupSerializer


class Employess(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = SignupSerializer

    def get_queryset(self):
        return User.objects.filter(type=User.UserType.EMPLOYEE)


class Account(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer


class CustomPagination(PageNumberPagination):
    max_page_size = 20
    page_size = 20

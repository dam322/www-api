from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',
                  'type',
                  'first_name',
                  'last_name',
                  'cell_phone',
                  'birth_day',
                  'direction',
                  'city')


class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ('token', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True
            },
        }

    def validate(self, data):
        user = get_object_or_404(User, email=data['email'])
        if not user.check_password(raw_password=data['password']):
            raise ValidationError("Contraseña incorrecta", status.HTTP_400_BAD_REQUEST)

        token, _ = Token.objects.get_or_create(user=user)
        data['token'] = token
        return data

from django.contrib.auth.password_validation import validate_password
from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError

from apps.users.models import User


class SmallUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',
                  'type',
                  'first_name',
                  'last_name',
                  'cell_phone',
                  'birth_day',
                  'direction',
                  'city',
                  )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'email',
                  'type',
                  'first_name',
                  'last_name',
                  'cell_phone',
                  'birth_day',
                  'direction',
                  'city',
                  )


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


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email',
                  'type',
                  'first_name',
                  'last_name',
                  'cell_phone',
                  'birth_day',
                  'direction',
                  'city',
                  'password',
                  'password2')

        extra_kwargs = {"password": {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(
            email=validated_data['email'],
            type=validated_data['type'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            cell_phone=validated_data['cell_phone'],
            birth_day=validated_data['birth_day'],
            direction=validated_data['direction'],
            city=validated_data['city'],
            password=validated_data['password']
        )

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords doesn't match."})

        return attrs

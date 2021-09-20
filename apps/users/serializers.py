from rest_framework import serializers

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

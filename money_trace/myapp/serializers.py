from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import CustomUser


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ('id', 'email', 'username', 'last_name', 'password')


class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = CustomUser
        fields = ('id', 'email', 'username',  'last_name')
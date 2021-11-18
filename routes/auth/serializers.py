from rest_framework import serializers
from rest_framework_simplejwt.tokens import AccessToken
from app.models import User


class LoginSerializers(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()


class RegisterSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'auth_token', 'is_email_verified']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def get_auth_token(self, obj):
        return str(AccessToken.for_user(obj))


class AuthSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'avatar',
                  'is_admin', 'is_instructor', 'auth_token', 'is_email_verified']

    def get_auth_token(self, obj):
        return str(AccessToken.for_user(obj))

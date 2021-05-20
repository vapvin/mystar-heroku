from rest_framework import serializers
from profiles.models import Profile, ProfileStatus
from rest_framework import serializers
from django.contrib.auth.models import User

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class ProfileSerialzier(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = Profile
        fields = "__all__"


class ProfileAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("avatar",)


class ProfileStatusSerializer(serializers.ModelSerializer):
    user_profile = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Profile
        fields = "__all__"
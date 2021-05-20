from rest_framework import serializers
from .models import PictureModel


class PictureSerializer(serializers.ModelSerializer):

    thumb = serializers.ImageField(read_only=True)

    class Meta:
        model = PictureModel
        fields = "__all__"
        lookup_field = "slug"

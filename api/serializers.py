from rest_framework import serializers
from image_bank.models import Image, Tag, Licence, ImageBankUser
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class LicenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licence
        fields = ['id', 'name', 'description']


class ImageSerializer(TaggitSerializer, serializers.ModelSerializer):
    new_tags = TagListSerializerField()

    class Meta:
        model = Image
        fields = ['id', 'image', 'auteur', 'name', 'description', 'price', 'licence', 'new_tags', 'width', 'height']


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageBankUser
        fields = ['username']
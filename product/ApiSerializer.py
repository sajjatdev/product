from rest_framework import serializers
from .models import Collection,Product


class collectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Collection
        fields="__all__"


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model=Product
        fields="__all__"
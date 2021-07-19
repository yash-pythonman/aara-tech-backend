from rest_framework import serializers

from shop.models import Shop


class ShopSerializer(serializers.ModelSerializer):
    """
    Serializer created to validate and serialize shop create API payloads.
    """

    class Meta:
        model = Shop
        fields = ("name", "address", "lat", "long")


class LatLongSerializer(serializers.Serializer):
    """
    Serializer created to validate latitude and longitude.
    """

    lat = serializers.FloatField()
    long = serializers.FloatField()

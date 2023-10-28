from rest_framework import serializers


class PictureSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    url = serializers.URLField()
    link = serializers.URLField()


class SatPictureSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    link = serializers.URLField()
    created_at = serializers.DateTimeField()


class PictureByZoneRequestSerializer(serializers.Serializer):
    date = serializers.DateTimeField()
    geozone_id = serializers.IntegerField()

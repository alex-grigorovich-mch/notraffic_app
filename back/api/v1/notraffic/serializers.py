from django.db.models import Q
from rest_framework import serializers

from notraffic.models import Intersection, Street


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ["name"]
        read_only_fields = ("name",)


class UpdateIntersectionSerializer(serializers.Serializer):
    name = serializers.CharField(
        write_only=True,
        max_length=128,
        required=True,
        allow_null=False,
    )

    latitude = serializers.DecimalField(
        write_only=True,
        max_digits=9,
        decimal_places=6,
        min_value=-90,
        max_value=90,
        required=True,
        allow_null=False,
    )

    longitude = serializers.DecimalField(
        write_only=True,
        max_digits=9,
        decimal_places=6,
        min_value=-180,
        max_value=180,
        required=True,
        allow_null=False,
    )

    first_street = serializers.CharField(
        write_only=True,
        max_length=128,
        required=True,
        allow_null=False,
    )

    second_street = serializers.CharField(
        write_only=True,
        max_length=128,
        required=True,
        allow_null=False,
    )

    def validate(self, data):
        first_street_name = data.get("first_street")
        second_street_name = data.get("second_street")
        if not first_street_name:
            raise serializers.ValidationError("First street name is required.")
        if not second_street_name:
            raise serializers.ValidationError("Second street name is required.")
        if first_street_name == second_street_name:
            raise serializers.ValidationError("First street and second street cannot be the same.")
        return data


class CreateIntersectionSerializer(UpdateIntersectionSerializer):
    def validate(self, data):
        data = super().validate(data)
        first_street_name = data.get("first_street")
        second_street_name = data.get("second_street")
        latitude = data.get("latitude")
        longitude = data.get("longitude")
        if (
            Intersection.objects.filter(latitude=latitude, longitude=longitude)
            .filter(
                (Q(first_street__name=first_street_name) & Q(second_street__name=second_street_name))
                | (Q(first_street__name=second_street_name) & Q(second_street__name=first_street_name))
            )
            .exists()
        ):
            raise serializers.ValidationError(
                "An intersection with similar latitude, longitude and streets already exists."
            )
        return data


class ListGetIntersectionSerializer(serializers.ModelSerializer):
    first_street = serializers.CharField(source='first_street.name')
    second_street = serializers.CharField(source='second_street.name')

    class Meta:
        model = Intersection
        fields = (
            "id",
            "name",
            "latitude",
            "longitude",
            "first_street",
            "second_street",
        )
        read_only_fields = (
            "id",
            "name",
            "latitude",
            "longitude",
            "first_street",
            "second_street",
        )

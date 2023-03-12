from rest_framework import serializers, status

from .models import LocatieEnum, Manual, Building, Ronde


class LocatieEnumSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocatieEnum
        fields = '__all__'

    def create(self, validated_data):
        """
            Created a location record in the database or gives an already existing one
        """
        try:
            location, _ = LocatieEnum.objects.get_or_create(
                name=validated_data["name"]
            )
            return location
        except IntegrityError as e:
            raise serializers.ValidationError({"errors": str(e)})


class ManaulSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manual
        fields = '__all__'


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'


class RondeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ronde
        fields = '__all__'

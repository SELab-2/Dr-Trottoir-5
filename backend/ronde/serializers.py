from rest_framework import serializers, status

from .models import LocatieEnum, Manual, Building, Ronde


class LocatieEnumSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocatieEnum
        fields = '__all__'

    def validate(self, data):
        if "name" not in data:
            raise serializers.ValidationError({"error": "Er is geen field 'name' meegeven"},
                                              code=status.HTTP_402_PAYMENT_REQUIRED)
        elif data['name'] == '':
            raise serializers.ValidationError({"error": "Field 'name' is leeg"}, code=status.HTTP_400_BAD_REQUEST)
        return data

    def create(self, validated_date):
        try:
            location = LocatieEnum.objects.create(
                name=validated_date["name"]
            )
            location.save()
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

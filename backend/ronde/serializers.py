from rest_framework import serializers

from .models import LocatieEnum, Manual, Building, Ronde


class LocatieEnumSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocatieEnum
        fields = '__all__'

    def validate(self, data):
        if 'name' not in data:
            return serializers.ValidationError({"error": "Er is geen field 'name' meegeven", 'status': 402})
        elif data['name'] == '':
            return serializers.ValidationError({"error": "Field 'name' is leeg", 'status' : 400})
        return super().validate(data)

    def create(self, validated_date):
        try:
            location = LocatieEnum.objects.create(
                name=validated_date["name"]
            )
            location.save()
            return location
        except IntegrityError as e:
            return serializers.ValidationError({"errors": str(e)})


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

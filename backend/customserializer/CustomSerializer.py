from rest_framework import serializers

class CustomSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        errors = []
        for field in self.required_fields:
            if attrs.get(field) is None:
                errors.append({
                    "message": "is required",
                    "field": field
                })
        if len(errors) > 0:
            raise serializers.ValidationError({
                "errors" : errors
            })
        return attrs
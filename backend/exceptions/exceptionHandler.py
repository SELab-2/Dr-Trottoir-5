from datetime import datetime

from rest_framework import serializers


class ExceptionHandler:
    required_error = "Veld is vereist."
    invalid_enum_choice_error = "Geen geldige keuze."
    pk_does_not_exist_error = "Object bestaat niet."
    date_format_error = "Datum heeft verkeerde formaat, gebruik: JJJJ-MM-DD."
    datetime_format_error = "Tijd heeft verkeerde formaat, gebruik: JJJJ-MM-DD " \
                        "uu:mm."
    time_format_error = "Tijd heeft verkeerde formaat, gebuik: uu:mm."
    file_upload_error = "Data is geen bestand."
    blank_error = "Veld kan niet leeg zijn."
    integer_error = "Veld moet een positief getal zijn."

    def __init__(self):
        self.errors = []

    def check(self):
        if len(self.errors) > 0:
            raise serializers.ValidationError({
                "errors": self.errors
            })

    def checkRequired(self, value, fieldName):
        if value is None:
            self.errors.append({
                "message": ExceptionHandler.required_error,
                "field": fieldName
            })
            return False
        return True

    def checkEnumValue(self, value, fieldname, enumValues):
        if self.checkRequired(value, fieldname) and value not in enumValues:
            self.errors.append({
                "message": ExceptionHandler.invalid_enum_choice_error,
                "field": fieldname
            })
            return False
        return True

    def checkTimeValue(self, value, fieldname):
        if not self.checkRequired(value, fieldname):
            return False
        try:
            datetime.strptime(value, "%H:%M")
        except ValueError:
            self.errors.append({
                "message": ExceptionHandler.time_format_error,
                "field": fieldname
            })
        return True


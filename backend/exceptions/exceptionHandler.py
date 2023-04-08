from datetime import datetime

from rest_framework import serializers

from django.db import models


class ExceptionHandler:
    """
    will raise errors if checks fail and object goes out of scope
    """
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
        self.checked = False

    def check(self):
        self.checked = True
        if len(self.errors) > 0:
            raise serializers.ValidationError({
                "errors": self.errors
            })

    def __del__(self):
        if not self.checked:
            self.check()

    def checkRequired(self, value, fieldName):
        self.checked = False
        if value is None:
            self.errors.append({
                "message": ExceptionHandler.required_error,
                "field": fieldName
            })
            return False
        return True

    def timeFormatChecker(self, value, fieldname, format, message):
        self.checked = False
        try:
            datetime.strptime(value, format)
        except ValueError:
            self.errors.append({
                "message": message,
                "field": fieldname
            })
            return False
        return True

    def checkEnumValue(self, value, fieldname, enumValues):
        """
        Will call checkRequired()
        will only add enum exception if value is not None
        Parameters
        ----------
        value
        fieldname
        enumValues

        Returns
        -------

        """
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
        return self.timeFormatChecker(value, fieldname, "%H:%M",
                                      ExceptionHandler.time_format_error)

    def checkDateValue(self, value, fieldname):
        if not self.checkRequired(value, fieldname):
            return False
        return self.timeFormatChecker(value, fieldname, "%Y-%m-%d",
                                      ExceptionHandler.date_format_error)

    def checkDateTimeValue(self, value, fieldname):
        if not self.checkRequired(value, fieldname):
            return False
        return self.timeFormatChecker(value, fieldname, "%Y-%m-%d %H:%M",
                                      ExceptionHandler.datetime_format_error)

    def checkPKValue(self, value, fieldname, cls: models.Model):
        print(cls)
        if not self.checkRequired(value, fieldname):
            return False
        try:
            cls.objects.get(pk=value)
            return True
        except ValueError:
            self.errors.append({
                "message": ExceptionHandler.pk_does_not_exist_error,
                "field": fieldname
            })
            return False
        except cls.DoesNotExist:
            self.errors.append({
                "message": ExceptionHandler.pk_does_not_exist_error,
                "field": fieldname
            })
            return False

    def checkFile(self, value, fieldname, files):
        if not self.checkRequired(value, fieldname):
            return False
        if value not in files.getlist(fieldname):
            self.errors.append({
                "message": ExceptionHandler.file_upload_error,
                "field": fieldname
            })
            return False
        return True

    def checkInteger(self, value, fieldname):
        if not self.checkRequired(value, fieldname):
            return False
        try:
            int(value)
            return True
        except ValueError:
            self.errors.append({
                "message": ExceptionHandler.integer_error,
                "field": fieldname
            })
            return False

    def checkNotBlank(self, value, fieldname):
        if not self.checkRequired(value, fieldname):
            return False
        value: str
        if value == "":
            self.errors.append({
                "message": ExceptionHandler.blank_error,
                "field": fieldname
            })
            return False
        return True

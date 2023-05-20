from datetime import datetime

from django.db import models
from rest_framework.serializers import ValidationError

from trashtemplates.models import Status


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
    boolean_error = "Veld moet een Boolse waarde zijn."
    wrong_email_error = "Verkeerd email adres."
    not_equal_error = "Waarde komt niet overeen."
    inactive_error = "Object is verwijderd."
    vervangen_error = "Kan geen aanpassingen doen aan vervangen template"

    def __init__(self):
        self.errors = []
        self.checked = False

    def check(self):
        self.checked = True
        if len(self.errors) > 0:
            raise ValidationError({
                "errors": self.errors
            }, code='invalid')

    def __del__(self):
        if not self.checked:
            self.check()

    def check_required(self, value, fieldName):
        self.checked = False
        if value is None:
            self.errors.append({
                "message": ExceptionHandler.required_error,
                "field": fieldName
            })
            return False
        return True

    def check_time_format(self, value, fieldname, format, message):
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

    def check_enum_value(self, value, fieldname, enumValues):
        self.checked = False
        if value is None:
            return True
        if value not in enumValues:
            self.errors.append({
                "message": ExceptionHandler.invalid_enum_choice_error,
                "field": fieldname
            })
            return False
        return True

    def check_enum_value_required(self, value, fieldname, enumValues):
        if not self.check_required(value, fieldname):
            return False
        return self.check_enum_value(value, fieldname, enumValues)

    def check_time_value(self, value, fieldname):
        self.checked = False
        if value is None:
            return True
        return self.check_time_format(value, fieldname, "%H:%M",
                                      ExceptionHandler.time_format_error)

    def check_time_value_required(self, value, fieldname):
        if not self.check_required(value, fieldname):
            return False
        return self.check_time_value(value, fieldname)

    def check_date_value(self, value, fieldname):
        self.checked = False
        if value is None:
            return True
        return self.check_time_format(value, fieldname, "%Y-%m-%d",
                                      ExceptionHandler.date_format_error)

    def check_date_value_required(self, value, fieldname):
        if not self.check_required(value, fieldname):
            return False
        return self.check_date_value(value, fieldname)

    def check_date_time_value(self, value, fieldname):
        self.checked = False
        if value is None:
            return True
        return self.check_time_format(value, fieldname, "%Y-%m-%d %H:%M",
                                      ExceptionHandler.datetime_format_error)

    def check_date_time_value_required(self, value, fieldname):
        if not self.check_required(value, fieldname):
            return False
        return self.check_date_time_value(value, fieldname)

    def check_primary_key(self, value, fieldname, cls: models.Model):
        self.checked = False
        if value is None:
            return True
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

    def check_primary_key_value_required(self, value, fieldname,
                                         cls: models.Model):
        if not self.check_required(value, fieldname):
            return False
        return self.check_primary_key(value, fieldname, cls)

    def check_file(self, value, fieldname, files):
        self.checked = False
        if value is None:
            return True
        if value not in files.getlist(fieldname):
            self.errors.append({
                "message": ExceptionHandler.file_upload_error,
                "field": fieldname
            })
            return False
        return True

    def check_file_required(self, value, fieldname, files):
        if not self.check_required(value, fieldname):
            return False
        return self.check_file(value, fieldname, files)

    def check_integer(self, value, fieldname):
        self.checked = False
        if value is None:
            return True
        try:
            int(value)
            return True
        except ValueError:
            self.errors.append({
                "message": ExceptionHandler.integer_error,
                "field": fieldname
            })
            return False

    def check_integer_required(self, value, fieldname):
        if not self.check_required(value, fieldname):
            return False
        return self.check_integer(value, fieldname)

    def check_boolean(self, value, fieldname):
        self.checked = False
        if value is None:
            return True
        try:
            bool(value)
            return True
        except ValueError:
            self.errors.append({
                "message": ExceptionHandler.boolean_error,
                "field": fieldname
            })
            return False

    def check_boolean_required(self, value, fieldname):
        if not self.check_required(value, fieldname):
            return False
        return self.check_boolean(value, fieldname)

    def check_not_blank(self, value, fieldname):
        self.checked = False
        if value is None:
            return True
        value: str
        if value == "":
            self.errors.append({
                "message": ExceptionHandler.blank_error,
                "field": fieldname
            })
            return False
        return True

    def check_not_blank_required(self, value, fieldname):
        if not self.check_required(value, fieldname):
            return False
        return self.check_not_blank(value, fieldname)

    def check_email(self, email, cls: models.Model):
        self.checked = False
        if email is None:
            return True
        try:
            cls.objects.get(email=email)
            return True
        except cls.DoesNotExist:
            self.errors.append({
                "message": ExceptionHandler.wrong_email_error,
                "field": "email"
            })
            return False

    def check_equal(self, value1, value2, fieldname):
        self.checked = False

        if value1 != value2:
            self.errors.append({
                "message": ExceptionHandler.not_equal_error,
                "field": fieldname
            })
            return False
        return True

    def check_not_inactive(self, template, fieldname):
        self.checked = False
        if template is None:
            return True

        if template.status == Status.INACTIEF:
            self.errors.append({
                "message": ExceptionHandler.inactive_error,
                "field": fieldname
            })
            return False

    def check_vervangen(self, template):
        self.checked = False
        if template is None:
            return True

        if template.status == Status.VERVANGEN:
            self.errors.append({
                "message": ExceptionHandler.vervangen_error,
                "field": "template"
            })
            return False

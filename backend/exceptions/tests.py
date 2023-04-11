from django.test import TestCase

from django.utils.datastructures import MultiValueDict

from rest_framework.serializers import ValidationError

from pickupdays.models import PickUpDay
from planning.models import WeekPlanning
from .exceptionHandler import ExceptionHandler
from model_bakery import baker


class ExceptionHandlerTest(TestCase):

    def setUp(self) -> None:
        self.wp = baker.make(WeekPlanning, week=0, year=2023)

    def test_required_success(self):
        handler = ExceptionHandler()
        self.assertTrue(handler.check_required("Value", "Value"))

    def test_required_fail(self):
        handler = ExceptionHandler()
        self.assertFalse(handler.check_required(None, ""))
        self.assertRaises(ValidationError, handler.check)

    def test_time_format_success(self):
        handler = ExceptionHandler()
        self.assertTrue(handler.check_time_format("07:05", "time", "%H:%M",
                                                  ""))

    def test_time_format_fail(self):
        handler = ExceptionHandler()
        self.assertFalse(
            handler.check_time_format("07-05", "time", "%H:%M", ""))
        self.assertRaises(ValidationError, handler.check)

    def test_enum_value_success(self):
        handler = ExceptionHandler()
        self.assertTrue(handler.check_enum_value("MO", "name",
                                                 PickUpDay.WeekDayEnum.values))

    def test_enum_value_fail_none(self):
        handler = ExceptionHandler()
        self.assertFalse(handler.check_enum_value(None, "name",
                                                  PickUpDay.WeekDayEnum.values))
        self.assertRaises(ValidationError, handler.check)

    def test_enum_value_fail_bad_value(self):
        handler = ExceptionHandler()
        self.assertFalse(handler.check_enum_value("Bad Value", "name",
                                                  PickUpDay.WeekDayEnum.values))
        self.assertRaises(ValidationError, handler.check)

    def test_time_value_success(self):
        handler = ExceptionHandler()
        self.assertTrue(handler.check_time_value("07:05", "name"))

    def test_time_value_fail_none(self):
        handler = ExceptionHandler()
        self.assertFalse(handler.check_time_value(None, "name"))
        self.assertRaises(ValidationError, handler.check)

    def test_time_value_fail_bad_value(self):
        handler = ExceptionHandler()
        self.assertFalse(handler.check_time_value("42", "name"))
        self.assertRaises(ValidationError, handler.check)

    def test_date_value_success(self):
        handler = ExceptionHandler()
        self.assertTrue(handler.check_date_value("2010-02-15", "name"))

    def test_date_value_fail_none(self):
        handler = ExceptionHandler()
        self.assertFalse(handler.check_date_value(None, "name"))
        self.assertRaises(ValidationError, handler.check)

    def test_date_value_fail_bad_value(self):
        handler = ExceptionHandler()
        self.assertFalse(handler.check_date_value("2010:05-15", "name"))
        self.assertRaises(ValidationError, handler.check)

    def test_date_time_value_success(self):
        handler = ExceptionHandler()
        self.assertTrue(handler.check_date_time_value("2010-05-13 07:35",
                                                      "name"))

    def test_date_time_value_fail_none(self):
        handler = ExceptionHandler()
        self.assertFalse(handler.check_date_time_value(None, "name"))
        self.assertRaises(ValidationError, handler.check)

    def test_date_time_value_fail_bad_value(self):
        handler = ExceptionHandler()
        self.assertFalse(handler.check_date_time_value("2010:05:13 07-35",
                                                       "name"))
        self.assertRaises(ValidationError, handler.check)

    def test_primary_key_value_success(self):
        handler = ExceptionHandler()
        self.assertTrue(handler.check_primary_key_value(self.wp.id, "name",
                                                        WeekPlanning))

    def test_primary_key_value_fail_none(self):
        handler = ExceptionHandler()
        self.assertFalse(handler.check_primary_key_value(None, "name", None))
        self.assertRaises(ValidationError, handler.check)

    def test_primary_key_value_fail_bad_value(self):
        handler = ExceptionHandler()
        self.assertFalse(
            handler.check_primary_key_value(42, "name", WeekPlanning))
        self.assertRaises(ValidationError, handler.check)

    def test_primary_key_value_fail_bad_type(self):
        handler = ExceptionHandler()
        self.assertFalse(
            handler.check_primary_key_value("test", "name", WeekPlanning))
        self.assertRaises(ValidationError, handler.check)

    def test_file_success(self):
        handler = ExceptionHandler()
        files = MultiValueDict({"name": ["filefield"]})
        self.assertTrue(handler.check_file("filefield", "name", files))

    def test_file_fail_none(self):
        handler = ExceptionHandler()
        files = MultiValueDict({"name": ["filefield"]})
        self.assertFalse(handler.check_file(None, "name", files))
        self.assertRaises(ValidationError, handler.check)

    def test_file_fail_bad_value(self):
        handler = ExceptionHandler()
        files = MultiValueDict({"name": ["a file name"]})
        self.assertFalse(handler.check_file("definitely not a file name",
                                            "name",
                                            files))
        self.assertRaises(ValidationError, handler.check)

    def test_integer_success(self):
        handler = ExceptionHandler()
        self.assertTrue(handler.check_integer(42, "name"))

    def test_integer_fail_none(self):
        handler = ExceptionHandler()
        self.assertFalse(handler.check_integer(None, "name"))
        self.assertRaises(ValidationError, handler.check)

    def test_integer_fail_bad_value(self):
        handler = ExceptionHandler()
        self.assertFalse(handler.check_integer("no integer", "name"))
        self.assertRaises(ValidationError, handler.check)

    def test_not_blank_success(self):
        handler = ExceptionHandler()
        self.assertTrue(handler.check_not_blank("not blank", "name"))

    def test_not_blank_fail_none(self):
        handler = ExceptionHandler()
        self.assertFalse(handler.check_not_blank(None, "name"))
        self.assertRaises(ValidationError, handler.check)

    def test_not_blank_fail_bad_value(self):
        handler = ExceptionHandler()
        self.assertFalse(handler.check_not_blank("", "name"))
        self.assertRaises(ValidationError, handler.check)

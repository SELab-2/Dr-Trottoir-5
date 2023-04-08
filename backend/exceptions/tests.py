from django.test import TestCase

from rest_framework.serializers import ValidationError

from pickupdays.models import PickUpDay
from .exceptionHandler import ExceptionHandler


class ExceptionHandlerTest(TestCase):

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



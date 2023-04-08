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
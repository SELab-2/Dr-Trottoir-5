from django.test import TestCase
from django.core.exceptions import ValidationError
from trashcontainers.models import TrashContainer
import datetime


class TrashContainerTestCase(TestCase):
    """
        Test if the trashcontainer model behaves as intended
    """

    def setUp(self):
        pass

    def test_start_hour(self):
        """
            Make sure we can't create a trashcontainer object where the starting hour
            is greater than the ending hour
        """
        with self.assertRaises(ValidationError):
            TrashContainer.objects.create(type="PM",
                                          start_hour=datetime.time(12, 00),
                                          end_hour=datetime.time(11, 00))

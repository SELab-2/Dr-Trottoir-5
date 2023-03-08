from django.test import TestCase
from rest_framework import serializers
from .serializers import TrashContainerSerializer
from .models import Weekday


class TrashContainerTestCase(TestCase):
    """
        Test if the trashcontainer model behaves as intended
    """

    def setUp(self):
        monday = Weekday.objects.create(weekday='MO').pk
        self.serializer_data_empty_collection_days = {
            "type": "PM",
            "collection_days": [],
            "start_hour": "11:00",
            "end_hour": "12:00"
        }
        self.serializer_data = {
            "type": "PM",
            "collection_days": [monday],
            "start_hour": "13:00",
            "end_hour": "12:00"
        }

    def test_empty_collection_days(self):
        """
            Serializer should not be valid if collection_days is empty
        """
        with self.assertRaisesMessage(serializers.ValidationError, "This list may not be empty."):
            TrashContainerSerializer(data=self.serializer_data_empty_collection_days).is_valid(raise_exception=True)

    def test_start_hour(self):
        """
            Make sure we can't create a trashcontainer object where the starting hour
            is greater than the ending hour
        """
        with self.assertRaisesMessage(serializers.ValidationError, "Start hour should not be later than end hour"):
            TrashContainerSerializer(data=self.serializer_data).is_valid(raise_exception=True)

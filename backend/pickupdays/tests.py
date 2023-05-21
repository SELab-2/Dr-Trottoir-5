from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from .models import PickUpDay
from .views import PickUpListCreateView, PickUpDetailView
from users.models import User


class TestApi(TestCase):
    def setUp(self):
        self.user = User.objects.create(role="SU")

    def testCreatePickupDay(self):
        """
        Test for creating a pickup day object
        """
        factory = APIRequestFactory()
        request = factory.post('/api/pickupdays/', {})
        force_authenticate(request, user=self.user)
        response = PickUpListCreateView.as_view()(request).data

        # Test if errors are returned if request body is incomplete
        self.assertIn("errors", response)

        request = factory.post('/api/pickupdays/', {"day": "MO", "start_hour": "12:00", "end_hour": "13:00"})
        force_authenticate(request, user=self.user)
        response = PickUpListCreateView.as_view()(request).data
        self.assertEqual(response["day"], "MO")

    def testComparePickupDays(self):
        day1 = PickUpDay.objects.create(day="MO", start_hour="12:00", end_hour="13:00")
        day2 = PickUpDay.objects.create(day="MO", start_hour="11:00", end_hour="13:00")
        day3 = PickUpDay.objects.create(day="MO", start_hour="12:00", end_hour="13:00")
        self.assertLess(day2, day1)
        self.assertEqual(day1, day3)

    def testPickupdayPatch(self):
        obj = PickUpDay.objects.create(day="MO", start_hour="12:00", end_hour="13:00")
        factory = APIRequestFactory()
        request = factory.patch(f'/api/pickupdays/{obj.pk}/', {"day": "TU"})
        force_authenticate(request, user=self.user)
        response = PickUpDetailView.as_view()(request, pk=obj.pk).data
        self.assertEqual(response["day"], "TU")

    def testPickupdayPut(self):
        obj = PickUpDay.objects.create(day="MO", start_hour="12:00", end_hour="13:00")
        factory = APIRequestFactory()
        request = factory.put(f'/api/pickupdays/{obj.pk}/', {"day": "MO", "start_hour": "14:15", "end_hour": "13:15"})
        force_authenticate(request, user=self.user)
        response = PickUpDetailView.as_view()(request, pk=obj.pk).data
        self.assertIn("start_hour", response)
